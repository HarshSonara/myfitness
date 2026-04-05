# MyFitness - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### 1. Server is Already Running! ✅
Your Django server is running at: **http://127.0.0.1:8000/**

### 2. Access the Application

#### Homepage
Visit: http://127.0.0.1:8000/
- View features, plans, and exercises
- Beautiful purple-pink gradient design
- Click "Get Started" to sign up

#### Admin Panel
Visit: http://127.0.0.1:8000/admin/
```
Username: admin
Password: admin123
```

### 3. Test User Registration

1. Go to http://127.0.0.1:8000/
2. Click "Sign Up" button
3. Fill in the form:
   - Username: testuser
   - Email: test@example.com
   - Password: Test@123456
   - Gender: Male/Female
   - Date of Birth: 01/01/2000
4. Click "Create Account"
5. You'll be redirected to dashboard

### 4. Test Login

1. Go to http://127.0.0.1:8000/
2. Click "Login" button
3. Enter credentials:
   - Email: test@example.com
   - Password: Test@123456
4. Click "Sign In"
5. Dashboard opens

### 5. Test Password Reset

1. Go to http://127.0.0.1:8000/
2. Click "Login" button
3. Click "Forgot Password?"
4. Enter your email address
5. Check your email inbox (sonaraharsh791@gmail.com)
6. Click the reset link in email
7. Set new password
8. Login with new password

### 6. Browse Exercises

1. Click "Exercises" in navigation
2. View all exercises with images
3. Click "View Details" on any exercise
4. Watch YouTube video tutorial
5. See exercise information

### 7. Admin Panel Features

1. Login to admin panel
2. Manage:
   - Users and profiles
   - Exercises (add YouTube URLs)
   - Subscription plans
   - Diet charts and meals
   - Workout logs
   - Progress tracking

---

## 🎨 Design Features

### Color Scheme
- Primary Purple: #667eea
- Dark Purple: #764ba2
- Pink: #f093fb
- Coral: #f5576c

### Pages Redesigned
✅ Homepage - Complete redesign with animations  
✅ Dashboard - Light theme with purple accents  
✅ Authentication - Unified login/signup page  
✅ Exercise List - Modern cards with filters  
✅ Exercise Detail - YouTube video integration  
✅ Password Reset - 4-page flow with email  

---

## 📧 Email Configuration

### Gmail SMTP Settings
- **Email**: sonaraharsh791@gmail.com
- **App Password**: ftbcalkoivjlgvxs
- **Status**: ✅ Configured and working

### Test Email Sending
1. Go to password reset page
2. Enter any registered email
3. Email will be sent via Gmail
4. Check inbox for reset link

---

## 🔧 Quick Commands

### Start Server (if stopped)
```bash
python manage.py runserver
```

### Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

### Make Migrations (if models change)
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect Static Files (for production)
```bash
python manage.py collectstatic
```

---

## 📱 Key URLs

| Page | URL |
|------|-----|
| Homepage | http://127.0.0.1:8000/ |
| Login/Signup | http://127.0.0.1:8000/signin/ |
| Dashboard | http://127.0.0.1:8000/dashboard/ |
| Exercises | http://127.0.0.1:8000/exercises/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |
| Password Reset | http://127.0.0.1:8000/password-reset/ |

---

## ✅ What's Working

- [x] User registration and login
- [x] Password reset with email
- [x] Dashboard with metrics
- [x] Exercise browsing
- [x] YouTube video integration
- [x] Admin panel
- [x] Beautiful UI design
- [x] Responsive layout
- [x] All animations
- [x] Email sending via Gmail

---

## 🎯 Next Steps

### For Testing
1. Create a few test user accounts
2. Add more exercises in admin panel
3. Test password reset flow
4. Browse all pages
5. Test on mobile devices

### For Production
1. Change SECRET_KEY in settings.py
2. Set DEBUG = False
3. Configure allowed hosts
4. Use PostgreSQL instead of SQLite
5. Set up proper email service
6. Configure static file serving
7. Add SSL certificate
8. Deploy to hosting service

---

## 🆘 Troubleshooting

### Server Not Running?
```bash
python manage.py runserver
```

### Static Files Not Loading?
1. Clear browser cache (Ctrl + Shift + R)
2. Try incognito mode
3. Run: `python manage.py collectstatic`

### Email Not Sending?
1. Check Gmail app password is correct
2. Verify 2-factor authentication is enabled
3. Check spam folder
4. Verify EMAIL_BACKEND in settings.py

### Database Errors?
```bash
python manage.py migrate
```

---

## 📞 Support

For detailed information, see:
- **FINAL_PROJECT_SUMMARY.md** - Complete project documentation
- **COLOR_PALETTE.md** - Design color scheme
- **GMAIL_SETUP_GUIDE.md** - Email configuration guide

---

**Status**: ✅ Everything is working perfectly!  
**Server**: http://127.0.0.1:8000/  
**Enjoy your fitness application!** 🎉💪
