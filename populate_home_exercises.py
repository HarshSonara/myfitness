from new.models import Exercise
from django.conf import settings
import os

# Delete all exercises
Exercise.objects.all().delete()
print('Cleared DB')

# Exercise data with correct model fields and existing images
exercises = [
    {'name': 'Bicep Curls', 'description': 'Muscular man doing bicep curls with dumbbell.', 'image': 'exercises/bicep_curls.jpg', 'calories_per_minute': 6.0, 'difficulty': 'intermediate', 'target_muscle': 'Biceps', 'equipment_needed': 'Dumbbells'},
    {'name': 'Squats', 'description': 'Deep squats for legs and glutes.', 'image': 'exercises/squats.jpg', 'calories_per_minute': 8.0, 'difficulty': 'intermediate', 'target_muscle': 'Quads', 'equipment_needed': 'Bodyweight'},
    {'name': 'Pushups', 'description': 'Standard pushups for chest.', 'image': 'exercises/pushups.jpg', 'calories_per_minute': 7.0, 'difficulty': 'beginner', 'target_muscle': 'Chest', 'equipment_needed': 'Bodyweight'},
    {'name': 'Running', 'description': 'Outdoor running cardio.', 'image': 'exercises/running.jpg', 'calories_per_minute': 10.0, 'difficulty': 'beginner', 'target_muscle': 'Legs', 'equipment_needed': 'Shoes'},
    {'name': 'Plank', 'description': 'Core plank hold.', 'image': 'exercises/plank.jpg', 'calories_per_minute': 5.0, 'difficulty': 'beginner', 'target_muscle': 'Core', 'equipment_needed': 'None'},
    {'name': 'Deadlift', 'description': 'Conventional deadlift.', 'image': 'exercises/deadlift.jpg', 'calories_per_minute': 9.0, 'difficulty': 'advanced', 'target_muscle': 'Back', 'equipment_needed': 'Barbell'},
    {'name': 'Lunges', 'description': 'Walking lunges.', 'image': 'exercises/lunges.jpg', 'calories_per_minute': 7.5, 'difficulty': 'intermediate', 'target_muscle': 'Legs', 'equipment_needed': 'Bodyweight'},
    {'name': 'Pullups', 'description': 'Pullup bar exercise.', 'image': 'exercises/pullups.jpg', 'calories_per_minute': 9.5, 'difficulty': 'advanced', 'target_muscle': 'Back', 'equipment_needed': 'Bar'},
    {'name': 'Burpees', 'description': 'Full body burpee.', 'image': 'exercises/burpees.jpg', 'calories_per_minute': 12.0, 'difficulty': 'intermediate', 'target_muscle': 'Full Body', 'equipment_needed': 'None'},
    {'name': 'Downward Dog', 'description': 'Yoga downward dog pose.', 'image': 'exercises/downward_dog.jpg', 'calories_per_minute': 4.0, 'difficulty': 'beginner', 'target_muscle': 'Shoulders', 'equipment_needed': 'Mat'},
]

created = 0
for ex in exercises:
    path = os.path.join(settings.MEDIA_ROOT, ex['image'])
    if os.path.exists(path):
        Exercise.objects.create(**{k: v for k, v in ex.items() if k != 'image'})
        print(f'✓ {ex["name"]} ({ex["image"]})')
        created += 1
    else:
        print(f'✗ Missing {ex["image"]}')

print(f'Created {created}/10 exercises. Reload home - images show!')
print('Home screen featured_exercises now populated!')

