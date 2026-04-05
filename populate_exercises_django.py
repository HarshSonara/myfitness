import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()

from new.models import Exercise
from django.conf import settings

# Clear existing exercises
Exercise.objects.all().delete()
print('Cleared DB')

# Exercise data
data = [
    {'name': 'Bicep Curls', 'description': 'Bicep curl with dumbbells', 'calories_per_minute': 6.0, 'difficulty': 'intermediate', 'target_muscle': 'Biceps', 'equipment_needed': 'Dumbbells', 'image': 'bicep_curls.jpg'},
    {'name': 'Squats', 'description': 'Bodyweight squats', 'calories_per_minute': 8.0, 'difficulty': 'intermediate', 'target_muscle': 'Quads', 'equipment_needed': 'Bodyweight', 'image': 'squats.jpg'},
    {'name': 'Pushups', 'description': 'Standard pushups', 'calories_per_minute': 7.0, 'difficulty': 'beginner', 'target_muscle': 'Chest', 'equipment_needed': 'Bodyweight', 'image': 'pushups.jpg'},
    {'name': 'Running', 'description': 'Jogging cardio', 'calories_per_minute': 10.0, 'difficulty': 'beginner', 'target_muscle': 'Legs', 'equipment_needed': 'Shoes', 'image': 'running.jpg'},
    {'name': 'Plank', 'description': 'Core plank', 'calories_per_minute': 5.0, 'difficulty': 'beginner', 'target_muscle': 'Core', 'equipment_needed': 'None', 'image': 'plank.jpg'},
    {'name': 'Deadlift', 'description': 'Barbell deadlift', 'calories_per_minute': 9.0, 'difficulty': 'advanced', 'target_muscle': 'Back', 'equipment_needed': 'Barbell', 'image': 'deadlift.jpg'},
    {'name': 'Lunges', 'description': 'Walking lunges', 'calories_per_minute': 7.5, 'difficulty': 'intermediate', 'target_muscle': 'Legs', 'equipment_needed': 'None', 'image': 'lunges.jpg'},
    {'name': 'Pullups', 'description': 'Pullup bar exercise', 'calories_per_minute': 9.5, 'difficulty': 'advanced', 'target_muscle': 'Back', 'equipment_needed': 'Pullup Bar', 'image': 'pullups.jpg'},
    {'name': 'Burpees', 'description': 'Full body burpee', 'calories_per_minute': 12.0, 'difficulty': 'intermediate', 'target_muscle': 'Full Body', 'equipment_needed': 'None', 'image': 'burpees.jpg'},
    {'name': 'Downward Dog', 'description': 'Yoga pose', 'calories_per_minute': 4.0, 'difficulty': 'beginner', 'target_muscle': 'Shoulders', 'equipment_needed': 'Mat', 'image': 'downward_dog.jpg'},
]

created = 0
for d in data:
    try:
        img_path = os.path.join(settings.MEDIA_ROOT, 'exercises', d['image'])
        if os.path.exists(img_path):
            Exercise.objects.create(**d)
            print(f'Created {d["name"]}')
            created += 1
        else:
            print(f'Missing image for {d["name"]}: {d["image"]}')
    except Exception as e:
        print(f'Error creating {d["name"]}: {e}')

print(f'Successfully created {created} exercises.')
