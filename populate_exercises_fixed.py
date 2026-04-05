from django.conf import settings
from new.models import Exercise
import os

# Clear existing exercises
Exercise.objects.all().delete()
print('Cleared DB')

# Exercise data with correct image paths
data = [
    dict(name='Bicep Curls', description='Muscular man doing bicep curls with dumbbell.', image='exercises/bicep_curls.jpg', calories_per_minute=6.0, difficulty='intermediate', target_muscle='Biceps', equipment_needed='Dumbbells'),
    dict(name='Squats', description='Deep squats for legs and glutes.', image='exercises/squats.jpg', calories_per_minute=8.0, difficulty='intermediate', target_muscle='Quads', equipment_needed='Bodyweight'),
    dict(name='Pushups', description='Standard pushups for chest.', image='exercises/pushups.jpg', calories_per_minute=7.0, difficulty='beginner', target_muscle='Chest', equipment_needed='Bodyweight'),
    dict(name='Running', description='Outdoor running cardio.', image='exercises/running.jpg', calories_per_minute=10.0, difficulty='beginner', target_muscle='Legs', equipment_needed='Shoes'),
    dict(name='Plank', description='Core plank hold.', image='exercises/plank.jpg', calories_per_minute=5.0, difficulty='beginner', target_muscle='Core', equipment_needed='None'),
    dict(name='Deadlift', description='Conventional deadlift.', image='exercises/deadlift.jpg', calories_per_minute=9.0, difficulty='advanced', target_muscle='Back', equipment_needed='Barbell'),
    dict(name='Lunges', description='Walking lunges.', image='exercises/lunges.jpg', calories_per_minute=7.5, difficulty='intermediate', target_muscle='Legs', equipment_needed='None'),
    dict(name='Pullups', description='Pullup bar exercise.', image='exercises/pullups.jpg', calories_per_minute=9.5, difficulty='advanced', target_muscle='Back', equipment_needed='Pullup Bar'),
    dict(name='Burpees', description='Full body burpee.', image='exercises/burpees.jpg', calories_per_minute=12.0, difficulty='intermediate', target_muscle='Full Body', equipment_needed='None'),
    dict(name='Downward Dog', description='Yoga downward dog pose.', image='exercises/downward_dog.jpg', calories_per_minute=4.0, difficulty='beginner', target_muscle='Shoulders', equipment_needed='Mat'),
]

# Create
for d in data:
    path = os.path.join(settings.MEDIA_ROOT, d['image'])
    if os.path.exists(path):
        exercise = Exercise.objects.create(**d)
        print(f"Created {d['name']} - image: {d['image']}")
    else:
        print(f'Missing image: {d["image"]}')

print('Done! 10 exercises created.')
