# MyFitness - Fitness & Diet Management System

A comprehensive Django-based fitness and diet management web application with a beautiful purple-pink gradient design.

![Django](https://img.shields.io/badge/Django-6.0.3-green.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### User Management
- ✅ User registration and authentication
- ✅ Profile management with health metrics
- ✅ Password reset via email (Gmail SMTP)
- ✅ Secure login/logout functionality

### Exercise System
- ✅ Browse 10+ exercises with images
- ✅ YouTube video integration for exercise tutorials
- ✅ Filter by difficulty, muscle group, equipment
- ✅ Detailed exercise information with calorie calculator

### Dashboard
- ✅ Modern light-themed dashboard
- ✅ Health metrics tracking (BMI, weight, calories)
- ✅ Recent activities overview
- ✅ Quick action buttons
- ✅ Weekly progress visualization

### Subscription Plans
- ✅ 3 subscription tiers (Basic, Premium, Elite)
- ✅ Instant activation system
- ✅ Plan comparison and features

### Tracking & Logging
- ✅ Workout logging with sets, reps, duration
- ✅ Meal logging with calorie tracking
- ✅ Progress tracking with body measurements
- ✅ Historical data visualization

### Admin Panel
- ✅ Comprehensive admin interface
- ✅ User management
- ✅ Exercise management with YouTube URLs
- ✅ Subscription plan management
- ✅ Diet chart and meal management

## 🎨 Design

### Color Palette
- **Primary Purple**: #667eea
- **Dark Purple**: #764ba2
- **Pink**: #f093fb
- **Coral**: #f5576c
- **Success Green**: #10b981
- **Warning Orange**: #f59e0b
- **Info Blue**: #3b82f6

### Design Features
- Purple-pink gradient theme throughout
- Glassmorphism effects
- Smooth animations (AOS library)
- Floating orb backgrounds
- Modern card designs
- Fully responsive layout
- Password strength indicators

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/myfitness.git
cd myfitness
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django==6.0.3
pip install pillow
pip install django-crispy-forms
pip install crispy-bootstrap5
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run the server**
```bash
python manage.py runserver
```

7. **Access the application**
- Homepage: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
myfitness1/
├── myproject/              # Django project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
│
├── new/                    # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # App URL routing
│   ├── forms.py            # Django forms
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   └── static/             # CSS, JS, images
│
├── media/                  # User uploads
├── static/                 # Static files
├── manage.py               # Django management
└── requirements.txt        # Python dependencies
```

## 🔧 Configuration

### Email Settings (Optional)

To enable password reset emails, update `myproject/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'MyFitness <your-email@gmail.com>'
```

### Database

By default, the project uses SQLite. For production, consider PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myfitness_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Database Models

- **User**: Django built-in user model
- **UserProfile**: Extended user information
- **HealthProfile**: Health metrics and goals
- **Exercise**: Exercise library with YouTube videos
- **WorkoutPlan**: Custom workout plans
- **WorkoutLog**: Workout tracking
- **Meal**: Meal database
- **MealLog**: Meal tracking
- **DietChart**: Diet plans
- **ProgressLog**: Progress tracking
- **Subscription**: Subscription plans
- **UserSubscription**: User subscriptions

## 🎯 Usage

### For Users

1. **Sign Up**: Create a new account
2. **Login**: Access your dashboard
3. **Setup Profile**: Complete health profile
4. **Browse Exercises**: View exercise library
5. **Subscribe**: Choose a subscription plan
6. **Log Activities**: Track workouts and meals
7. **Monitor Progress**: View your fitness journey

### For Administrators

1. **Access Admin Panel**: http://127.0.0.1:8000/admin/
2. **Manage Users**: View and edit user accounts
3. **Add Exercises**: Create new exercises with YouTube videos
4. **Create Plans**: Set up subscription plans
5. **Monitor Activity**: View logs and progress

## 🛠️ Technologies Used

### Backend
- Django 6.0.3
- Python 3.13
- SQLite (development)

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 5
- AOS (Animate On Scroll)
- Font Awesome Icons

### Features
- Django Authentication System
- Gmail SMTP Integration
- YouTube Video Embedding
- Responsive Design

## 📝 Sample Data

The project includes sample data:
- 10 exercises with images
- 3 subscription plans
- 3 diet charts
- 6 meal options

## 🔐 Security

- Passwords are hashed using Django's built-in system
- CSRF protection enabled
- Secure password reset with tokens
- Email verification for password reset

## 🚀 Deployment

### For Production

1. **Update settings.py**:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Change `SECRET_KEY`

2. **Use PostgreSQL**:
   - Install PostgreSQL
   - Update database settings

3. **Collect static files**:
```bash
python manage.py collectstatic
```

4. **Use a production server**:
   - Gunicorn
   - uWSGI
   - Nginx

5. **Deploy to**:
   - Heroku
   - DigitalOcean
   - AWS
   - PythonAnywhere

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Developer

**Harsh Sonara**
- Email: sonaraharsh791@gmail.com

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions, please open an issue on GitHub.

## 🎉 Acknowledgments

- Bootstrap for CSS framework
- Font Awesome for icons
- AOS for animations
- Django community for excellent documentation

---

**Status**: ✅ Production Ready  
**Version**: 2.0  
**Last Updated**: April 5, 2026

🎊 **Start your fitness journey today!** 💪
