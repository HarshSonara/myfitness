from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import UserProfile, HealthProfile, WorkoutLog, MealLog, ProgressLog

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dob', 'gender', 'mobile', 'address', 'profile_picture']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class HealthProfileForm(forms.ModelForm):
    class Meta:
        model = HealthProfile
        fields = ['age_group', 'height', 'weight', 'diseases', 'target_weight', 'fitness_goal']
        widgets = {
            'height': forms.NumberInput(attrs={'min': '50', 'max': '300', 'step': '0.1'}),
            'weight': forms.NumberInput(attrs={'min': '20', 'max': '500', 'step': '0.1'}),
            'target_weight': forms.NumberInput(attrs={'step': '0.1'}),
        }

    def calculate_bmi(self):
        height = self.cleaned_data.get('height')
        weight = self.cleaned_data.get('weight')
        if height and weight:
            height_m = float(height) / 100
            return round(float(weight) / (height_m ** 2), 1)
        return None

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['exercise', 'date', 'sets', 'reps', 'weight', 'duration_minutes', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class MealLogForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ['meal', 'date', 'quantity', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ProgressLogForm(forms.ModelForm):
    class Meta:
        model = ProgressLog
        fields = ['date', 'weight', 'body_fat_percentage', 'muscle_mass', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
