from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class HealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=30, choices=[('10-25', '10-25'), ('25-40', '25-40'), ('40-55', '40-55'), ('55-70', '55-70')])
    height = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(50), MaxValueValidator(300)])
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(20), MaxValueValidator(500)])
    diseases = models.CharField(max_length=30, choices=[('obesity', 'obesity'), ('cholesterol', 'cholesterol'), ('Heart health', 'Heart health'), ('Acidity', 'Acidity'), ('Blood Pressure', 'Blood Pressure'), ('Diabetes', 'Diabetes')], blank=True)
    target_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fitness_goal = models.TextField(blank=True, null=True)
    bmi = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Health"

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"

    @property
    def days_remaining(self):
        from datetime import date
        if self.end_date:
            remaining = (self.end_date - date.today()).days
            return max(0, remaining)
        return 0

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exercises/', blank=True, null=True)
    calories_per_minute = models.DecimalField(max_digits=5, decimal_places=2)
    difficulty = models.CharField(max_length=20, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner')
    target_muscle = models.CharField(max_length=50, blank=True, default="")
    equipment_needed = models.CharField(max_length=100, blank=True, default="")
    youtube_url = models.URLField(blank=True, null=True, help_text="YouTube video URL for exercise tutorial (e.g., https://www.youtube.com/watch?v=xxxxx)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_youtube_embed_url(self):
        """Convert YouTube URL to embed URL"""
        if self.youtube_url:
            # Handle embed URLs (already in correct format)
            if 'youtube.com/embed/' in self.youtube_url:
                # Extract video ID from embed URL
                video_id = self.youtube_url.split('youtube.com/embed/')[1].split('?')[0]
                return f'https://www.youtube.com/embed/{video_id}'
            # Handle standard watch URLs
            elif 'youtube.com/watch?v=' in self.youtube_url:
                video_id = self.youtube_url.split('watch?v=')[1].split('&')[0]
                return f'https://www.youtube.com/embed/{video_id}'
            # Handle short URLs
            elif 'youtu.be/' in self.youtube_url:
                video_id = self.youtube_url.split('youtu.be/')[1].split('?')[0]
                return f'https://www.youtube.com/embed/{video_id}'
        return None

class DietChart(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='diet_charts/', blank=True)
    meal_type = models.CharField(max_length=20, choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default='Lunch')
    age_group = models.CharField(max_length=20, choices=[('10-25', '10-25'), ('25-40', '25-40'), ('40-55', '40-55'), ('55-70', '55-70')])
    diseases = models.CharField(max_length=30, choices=[('obesity', 'obesity'), ('cholesterol', 'cholesterol'), ('Heart health', 'Heart health'), ('Acidity', 'Acidity'), ('Blood Pressure', 'Blood Pressure'), ('Diabetes', 'Diabetes')])
    calories = models.IntegerField(default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    diet_chart = models.ForeignKey(DietChart, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProgressLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    body_fat_percentage = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    duration_minutes = models.IntegerField(default=0)
    calories_burned = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} - {self.date}"

class MealLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    quantity = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)
    calories_consumed = models.DecimalField(max_digits=6, decimal_places=2)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.meal.name} - {self.date}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default='card')
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_id}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=25)
    amount = models.CharField(max_length=5)
    message = models.TextField()
    order_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if self.paid == True:
            return self.name + " paid"
        else:
            return self.name + " not paid"

