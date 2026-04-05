from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class HealthProfileInline(admin.StackedInline):
    model = HealthProfile
    can_delete = False
    verbose_name_plural = 'Health Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, HealthProfileInline)

# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'dob', 'gender', 'mobile', 'profile_picture']
    list_filter = ['gender']
    search_fields = ['user__username', 'user__email']

@admin.register(HealthProfile)
class HealthProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age_group', 'height', 'weight', 'diseases', 'bmi']
    list_filter = ['age_group', 'diseases']
    search_fields = ['user__username']

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'difficulty', 'target_muscle', 'calories_per_minute', 'has_video']
    list_filter = ['difficulty', 'target_muscle']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Exercise Details', {
            'fields': ('difficulty', 'target_muscle', 'equipment_needed', 'calories_per_minute')
        }),
        ('Video Tutorial', {
            'fields': ('youtube_url',),
            'description': 'Add YouTube video URL (e.g., https://www.youtube.com/watch?v=xxxxx or https://youtu.be/xxxxx)'
        }),
    )
    
    def has_video(self, obj):
        return bool(obj.youtube_url)
    has_video.boolean = True
    has_video.short_description = 'Video'

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration_days', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'start_date', 'end_date', 'is_active', 'payment_status']
    list_filter = ['is_active', 'payment_status', 'plan']
    search_fields = ['user__username', 'plan__name']

@admin.register(DietChart)
class DietChartAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan', 'meal_type', 'age_group', 'diseases', 'calories']
    list_filter = ['meal_type', 'age_group', 'diseases', 'plan']
    search_fields = ['name', 'description']

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'diet_chart', 'calories', 'protein', 'carbs', 'fat']
    list_filter = ['diet_chart__meal_type']
    search_fields = ['name', 'ingredients']

@admin.register(ProgressLog)
class ProgressLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'weight', 'body_fat_percentage', 'muscle_mass']
    list_filter = ['date']
    search_fields = ['user__username']

@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'exercise', 'date', 'sets', 'reps', 'weight', 'calories_burned']
    list_filter = ['date', 'exercise']
    search_fields = ['user__username', 'exercise__name']

@admin.register(MealLog)
class MealLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'meal', 'date', 'quantity', 'calories_consumed']
    list_filter = ['date']
    search_fields = ['user__username', 'meal__name']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription', 'amount', 'status', 'payment_date', 'transaction_id']
    list_filter = ['status', 'payment_method']
    search_fields = ['user__username', 'transaction_id']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'amount', 'paid']
    search_fields = ['name', 'email', 'order_id']
