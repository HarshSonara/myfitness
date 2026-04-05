from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum, Avg
from django.http import JsonResponse
import uuid

from .models import *  
from .forms import *  

@login_required
def dashboard(request):
    subscription = Subscription.objects.filter(user=request.user, is_active=True).first()
    health_profile_data = HealthProfile.objects.filter(user=request.user).values('weight', 'height', 'age_group', 'bmi').first()
    bmi = None
    if health_profile_data:
        if health_profile_data.get('bmi'):
            bmi = health_profile_data['bmi']
        elif health_profile_data.get('weight') and health_profile_data.get('height'):
            weight = float(health_profile_data['weight'])
            height = float(health_profile_data['height']) / 100  # Convert cm to meters
            if height > 0:
                bmi = round(weight / (height ** 2), 1)
                
    health_profile = {'weight': health_profile_data.get('weight') if health_profile_data else None, 'bmi': bmi, 'age_group': health_profile_data.get('age_group') if health_profile_data else None}
    recent_progress = ProgressLog.objects.filter(user=request.user)[:5]
    today_workouts = WorkoutLog.objects.filter(user=request.user, date=timezone.now().date()).select_related('exercise')
    today_meals = MealLog.objects.filter(user=request.user, date=timezone.now().date()).select_related('meal')
    today_calories_burned = today_workouts.aggregate(total=Sum('calories_burned'))['total'] or 0
    today_calories_consumed = today_meals.aggregate(total=Sum('calories_consumed'))['total'] or 0
    net_calories = today_calories_burned - today_calories_consumed
    
    context = {
        'subscription': subscription,
        'health_profile': health_profile,
        'recent_progress': recent_progress,
        'today_workouts': today_workouts,
        'today_meals': today_meals,
        'today_calories_burned': today_calories_burned,
        'today_calories_consumed': today_calories_consumed,
        'net_calories': net_calories,
    }
    return render(request, 'dashboard.html', context)

def exercise_list(request):
    exercises = Exercise.objects.all()
    search = request.GET.get('search', '')
    difficulty = request.GET.get('difficulty', '')
    muscle = request.GET.get('muscle', '')
    equipment = request.GET.get('equipment', '')

    if search:
        exercises = exercises.filter(name__icontains=search)
    if difficulty:
        exercises = exercises.filter(difficulty=difficulty)
    if muscle:
        exercises = exercises.filter(target_muscle__icontains=muscle)
    if equipment:
        exercises = exercises.filter(equipment_needed__icontains=equipment)

    exercises = exercises[:12]
    context = {'exercises': exercises, 'featured_exercises': exercises[:6]}
    return render(request, 'exercise_list.html', context)

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise.objects.only('name', 'description', 'image', 'calories_per_minute', 'difficulty', 'target_muscle', 'equipment_needed'), pk=pk)
    context = {'exercise': exercise}
    return render(request, 'exercise_detail.html', context)

@login_required
def plans(request):
    plans = SubscriptionPlan.objects.filter(is_active=True)
    context = {'plans': plans}
    return render(request, 'plans.html', context)

@login_required
def payment(request, plan_id):
    if request.method == 'POST':
        plan = get_object_or_404(SubscriptionPlan, id=plan_id)
        Subscription.objects.create(
            user=request.user,
            plan=plan,
            end_date=timezone.now() + timedelta(days=plan.duration_days),
            is_active=True,
            payment_status='completed'
        )
        messages.success(request, f'✅ {plan.name} activated instantly!')
        return redirect('dashboard')
    
    plan = get_object_or_404(SubscriptionPlan, id=plan_id, is_active=True)
    context = {
        'plan': plan,
        'amount': plan.price
    }
    return render(request, 'payment.html', context)

@login_required
def process_payment(request):
    if request.method == 'POST':
        messages.success(request, 'Payment successful! (Demo)')
        return redirect('dashboard')
    return redirect('plans')

def index(request):
    featured_plans = SubscriptionPlan.objects.filter(is_active=True)[:3]
    featured_exercises = Exercise.objects.only('name', 'description', 'difficulty', 'calories_per_minute', 'target_muscle', 'equipment_needed')[:6]
    
    # Get counts for statistics
    total_exercises = Exercise.objects.count()
    total_plans = SubscriptionPlan.objects.filter(is_active=True).count()

    context = {
        'featured_plans': featured_plans,
        'featured_exercises': featured_exercises,
        'total_exercises': total_exercises,
        'total_plans': total_plans,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'auth.html', {'tab': 'login'})

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        # Get form data from custom field names
        username = request.POST.get('name1')
        email = request.POST.get('email1')
        password = request.POST.get('password1')
        dob = request.POST.get('dob1')
        gender = request.POST.get('gender1')
        phone = request.POST.get('phone1')
        address = request.POST.get('address1')
        
        # Validate required fields
        if not username or not email or not password:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'auth.html', {'tab': 'signup'})
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return render(request, 'auth.html', {'tab': 'signup'})
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use another email or login.')
            return render(request, 'auth.html', {'tab': 'signup'})
        
        # Validate password length
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'auth.html', {'tab': 'signup'})
        
        try:
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Create user profile if additional data provided
            if dob or gender or phone or address:
                UserProfile.objects.create(
                    user=user,
                    dob=dob if dob else None,
                    gender=gender if gender else None,
                    mobile=phone if phone else None,
                    address=address if address else None
                )
            
            # Log the user in
            login(request, user)
            messages.success(request, f'Welcome {username}! Your account has been created successfully!')
            return redirect('dashboard')
            
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'auth.html', {'tab': 'signup'})
    
    return render(request, 'auth.html', {'tab': 'signup'})

@login_required
def profile_setup(request):
    if request.method == 'POST':
        try:
            profile_instance = UserProfile.objects.filter(user=request.user).first()
        except:
            profile_instance = None
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_instance)
        try:
            health_instance = HealthProfile.objects.filter(user=request.user).first()
        except:
            health_instance = None
        health_form = HealthProfileForm(request.POST, instance=health_instance)
        if profile_form.is_valid() and health_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            health = health_form.save(commit=False)
            health.user = request.user
            health.save()
            health.bmi = health_form.calculate_bmi()
            health.save()
            messages.success(request, 'Profile setup complete!')
            return redirect('dashboard')
    else:
        try:
            profile_instance = UserProfile.objects.filter(user=request.user).first()
        except:
            profile_instance = None
        profile_form = UserProfileForm(instance=profile_instance)
        try:
            health_instance = HealthProfile.objects.filter(user=request.user).first()
        except:
            health_instance = None
        health_form = HealthProfileForm(instance=health_instance)
    context = {'profile_form': profile_form, 'health_form': health_form}
    return render(request, 'profile_setup.html', context)

def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('index')

# Password Reset Views
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Create reset link
            reset_link = request.build_absolute_uri(f'/password-reset-confirm/{uid}/{token}/')
            
            # Send email
            try:
                subject = 'Password Reset - MyFitness'
                message = f'''
Hello {user.username},

You requested to reset your password for your MyFitness account.

Click the link below to reset your password:
{reset_link}

This link will expire after you use it once.

If you didn't request this, please ignore this email.

Best regards,
MyFitness Team
                '''
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Password reset email sent! Check your inbox.')
            except Exception as e:
                # If email fails, show the link (for development)
                messages.warning(request, f'Email sending failed. Reset link: {reset_link}')
                messages.info(request, 'Please configure email settings in settings.py')
            
            return redirect('password_reset_done')
        except User.DoesNotExist:
            messages.error(request, 'No user found with that email address.')
    
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password1 = request.POST.get('new_password1')
            password2 = request.POST.get('new_password2')
            
            if password1 and password2:
                if password1 == password2:
                    if len(password1) >= 8:
                        user.set_password(password1)
                        user.save()
                        messages.success(request, 'Password reset successful!')
                        return redirect('password_reset_complete')
                    else:
                        messages.error(request, 'Password must be at least 8 characters long.')
                else:
                    messages.error(request, 'Passwords do not match.')
            else:
                messages.error(request, 'Please fill in both password fields.')
        
        return render(request, 'password_reset_confirm.html', {'validlink': True})
    else:
        return render(request, 'password_reset_confirm.html', {'validlink': False})

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')

def four(request):
    return render(request, '404.html')

@login_required
def workout_logging(request):
    if request.method == 'POST':
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            if log.duration_minutes and log.exercise.calories_per_minute:
                log.calories_burned = log.duration_minutes * log.exercise.calories_per_minute
            log.save()
            messages.success(request, 'Workout logged successfully!')
            return redirect('dashboard')
    else:
        form = WorkoutLogForm()
    return render(request, 'workout_logging.html', {'form': form})

@login_required
def meal_logging(request):
    if request.method == 'POST':
        form = MealLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.calories_consumed = log.meal.calories * log.quantity
            log.save()
            messages.success(request, 'Meal logged successfully!')
            return redirect('dashboard')
    else:
        form = MealLogForm()
    return render(request, 'meal_logging.html', {'form': form})

@login_required
def progress_tracking(request):
    if request.method == 'POST':
        form = ProgressLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            messages.success(request, 'Progress logged successfully!')
            return redirect('dashboard')
    else:
        form = ProgressLogForm()
    logs = ProgressLog.objects.filter(user=request.user).order_by('-date')
    return render(request, 'progress_tracking.html', {'form': form, 'logs': logs})
