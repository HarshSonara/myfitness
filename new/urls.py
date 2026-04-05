from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('404/', views.four, name='404'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signin/', views.signin, name='signin'),
    path('register/', views.signup, name='register'),
    path('signup/', views.signup, name='signup'),  # Legacy template support
    path('login/', views.signin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Password Reset URLs
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset-done/', views.password_reset_done, name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete, name='password_reset_complete'),
    
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('plans/', views.plans, name='plans'),
    path('profile-setup/', views.profile_setup, name='profile_setup'),
    path('payment/<int:plan_id>/', views.payment, name='payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('workout-logging/', views.workout_logging, name='workout_logging'),
    path('meal_logging/', views.meal_logging, name='meal_logging'),
    path('progress-tracking/', views.progress_tracking, name='progress_tracking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
