import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from new.models import Exercise, SubscriptionPlan, DietChart, Meal
from datetime import timedelta
from django.utils import timezone

# Set admin password
admin = User.objects.get(username='admin')
admin.set_password('admin123')
admin.save()
print("✅ Admin password set to: admin123")

# Create Exercises
exercises_data = [
    {'name': 'Push-ups', 'description': 'Classic upper body exercise', 'difficulty': 'beginner', 'calories_per_minute': 7.0, 'target_muscle': 'Chest', 'equipment_needed': 'None'},
    {'name': 'Squats', 'description': 'Lower body strength exercise', 'difficulty': 'beginner', 'calories_per_minute': 8.0, 'target_muscle': 'Legs', 'equipment_needed': 'None'},
    {'name': 'Pull-ups', 'description': 'Upper body pulling exercise', 'difficulty': 'intermediate', 'calories_per_minute': 10.0, 'target_muscle': 'Back', 'equipment_needed': 'Pull-up bar'},
    {'name': 'Plank', 'description': 'Core strengthening exercise', 'difficulty': 'beginner', 'calories_per_minute': 5.0, 'target_muscle': 'Core', 'equipment_needed': 'None'},
    {'name': 'Burpees', 'description': 'Full body cardio exercise', 'difficulty': 'advanced', 'calories_per_minute': 12.0, 'target_muscle': 'Full Body', 'equipment_needed': 'None'},
    {'name': 'Lunges', 'description': 'Leg strengthening exercise', 'difficulty': 'beginner', 'calories_per_minute': 6.0, 'target_muscle': 'Legs', 'equipment_needed': 'None'},
    {'name': 'Deadlift', 'description': 'Compound strength exercise', 'difficulty': 'advanced', 'calories_per_minute': 9.0, 'target_muscle': 'Back', 'equipment_needed': 'Barbell'},
    {'name': 'Bicep Curls', 'description': 'Arm isolation exercise', 'difficulty': 'beginner', 'calories_per_minute': 4.0, 'target_muscle': 'Arms', 'equipment_needed': 'Dumbbells'},
    {'name': 'Running', 'description': 'Cardio endurance exercise', 'difficulty': 'beginner', 'calories_per_minute': 11.0, 'target_muscle': 'Legs', 'equipment_needed': 'None'},
    {'name': 'Yoga Downward Dog', 'description': 'Flexibility and strength', 'difficulty': 'beginner', 'calories_per_minute': 3.0, 'target_muscle': 'Full Body', 'equipment_needed': 'Yoga mat'},
]

for ex_data in exercises_data:
    Exercise.objects.get_or_create(name=ex_data['name'], defaults=ex_data)
print(f"✅ Created {len(exercises_data)} exercises")

# Create Subscription Plans
plans_data = [
    {'name': 'Basic Plan', 'description': 'Perfect for beginners starting their fitness journey', 'duration_days': 30, 'price': 499.00, 'features': ['Access to basic exercises', 'Diet tracking', 'Progress monitoring']},
    {'name': 'Premium Plan', 'description': 'Advanced features for serious fitness enthusiasts', 'duration_days': 90, 'price': 1299.00, 'features': ['All Basic features', 'Custom workout plans', 'Nutrition guidance', 'Priority support']},
    {'name': 'Elite Plan', 'description': 'Complete fitness transformation package', 'duration_days': 180, 'price': 2499.00, 'features': ['All Premium features', 'Personal trainer consultation', 'Custom meal plans', '24/7 support', 'Advanced analytics']},
]

for plan_data in plans_data:
    SubscriptionPlan.objects.get_or_create(name=plan_data['name'], defaults=plan_data)
print(f"✅ Created {len(plans_data)} subscription plans")

# Create Diet Charts
plan = SubscriptionPlan.objects.first()
if plan:
    diet_charts_data = [
        {'name': 'High Protein Breakfast', 'description': 'Protein-rich breakfast for muscle building', 'meal_type': 'Breakfast', 'age_group': '25-40', 'diseases': 'obesity', 'calories': 450, 'protein': 35.0, 'carbs': 40.0, 'fat': 15.0, 'plan': plan},
        {'name': 'Balanced Lunch', 'description': 'Well-balanced lunch for energy', 'meal_type': 'Lunch', 'age_group': '25-40', 'diseases': 'cholesterol', 'calories': 600, 'protein': 40.0, 'carbs': 60.0, 'fat': 20.0, 'plan': plan},
        {'name': 'Light Dinner', 'description': 'Light and healthy dinner option', 'meal_type': 'Dinner', 'age_group': '40-55', 'diseases': 'Diabetes', 'calories': 400, 'protein': 30.0, 'carbs': 35.0, 'fat': 12.0, 'plan': plan},
    ]
    
    for diet_data in diet_charts_data:
        diet_chart, created = DietChart.objects.get_or_create(name=diet_data['name'], defaults=diet_data)
        
        # Create meals for each diet chart
        if created:
            meals_data = [
                {'name': f'{diet_data["name"]} - Option 1', 'calories': diet_data['calories'], 'protein': diet_data['protein'], 'carbs': diet_data['carbs'], 'fat': diet_data['fat'], 'ingredients': 'Chicken, Rice, Vegetables', 'instructions': 'Cook and serve', 'diet_chart': diet_chart},
                {'name': f'{diet_data["name"]} - Option 2', 'calories': diet_data['calories'] - 50, 'protein': diet_data['protein'] - 5, 'carbs': diet_data['carbs'], 'fat': diet_data['fat'], 'ingredients': 'Fish, Quinoa, Salad', 'instructions': 'Grill and serve', 'diet_chart': diet_chart},
            ]
            for meal_data in meals_data:
                Meal.objects.create(**meal_data)
    
    print(f"✅ Created {len(diet_charts_data)} diet charts with meals")

print("\n" + "="*50)
print("🎉 DATABASE POPULATED SUCCESSFULLY!")
print("="*50)
print("\n📝 Login Credentials:")
print("   Username: admin")
print("   Password: admin123")
print("\n🌐 Access the application at: http://127.0.0.1:8000/")
print("🔐 Admin panel at: http://127.0.0.1:8000/admin/")
print("="*50)
