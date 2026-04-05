# ⚠️ IMPORTANT: Before Uploading to GitHub

## 🔒 Security Checklist

### 1. Remove Sensitive Data from settings.py

Open `myproject/settings.py` and make these changes:

#### Change SECRET_KEY:
```python
# BEFORE (Don't upload this!)
SECRET_KEY = 'django-insecure-actual-secret-key-here'

# AFTER (Safe to upload)
SECRET_KEY = 'your-secret-key-here-change-in-production'
```

#### Remove Email Credentials:
```python
# BEFORE (Don't upload this!)
EMAIL_HOST_USER = 'sonaraharsh791@gmail.com'
EMAIL_HOST_PASSWORD = 'ftbcalkoivjlgvxs'

# AFTER (Safe to upload)
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

Or better, use environment variables:
```python
import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your-email@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'your-app-password')
```

### 2. Verify .gitignore

Make sure these files are in `.gitignore`:
- ✅ `db.sqlite3` (your database with user data)
- ✅ `*.pyc` (Python cache files)
- ✅ `__pycache__/` (Python cache directories)
- ✅ `.env` (environment variables)
- ✅ `/media` (user uploaded files)
- ✅ `/staticfiles` (collected static files)

### 3. Remove Personal Data

Check these files and remove any personal information:
- Documentation files (.md files)
- Comments in code
- Test data with real emails/names

### 4. Database

Your `db.sqlite3` file contains:
- Admin credentials (admin/admin123)
- User accounts
- Personal data

**This file is already in .gitignore and won't be uploaded.**

Users who clone your repo will need to:
1. Run `python manage.py migrate`
2. Create their own superuser
3. Add their own data

---

## ✅ Quick Fix Commands

### Option 1: Manual Edit

1. Open `myproject/settings.py`
2. Find and replace:
   - SECRET_KEY value
   - EMAIL_HOST_USER value
   - EMAIL_HOST_PASSWORD value
3. Save the file

### Option 2: Use Environment Variables (Recommended)

1. Install python-decouple:
```bash
pip install python-decouple
```

2. Update `myproject/settings.py`:
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')
DEBUG = config('DEBUG', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
```

3. Create `.env` file (this won't be uploaded):
```
SECRET_KEY=your-actual-secret-key
DEBUG=True
EMAIL_HOST_USER=sonaraharsh791@gmail.com
EMAIL_HOST_PASSWORD=ftbcalkoivjlgvxs
```

4. Copy `.env.example` for others to use

---

## 📋 Pre-Upload Checklist

Before running `git push`:

- [ ] SECRET_KEY changed in settings.py
- [ ] Email credentials removed/hidden
- [ ] .gitignore file exists
- [ ] db.sqlite3 is in .gitignore
- [ ] No personal data in code comments
- [ ] README.md updated with your info
- [ ] requirements.txt is up to date
- [ ] All sensitive data removed

---

## 🔍 How to Check What Will Be Uploaded

Run this command to see what files will be uploaded:
```bash
git status
```

Files in red = will be uploaded  
Files not shown = ignored by .gitignore ✅

To see ignored files:
```bash
git status --ignored
```

---

## ⚡ Quick Security Fix

If you want to quickly fix settings.py, here's what to change:

### Find this section in myproject/settings.py:
```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-...'

# Email Configuration for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sonaraharsh791@gmail.com'
EMAIL_HOST_PASSWORD = 'ftbcalkoivjlgvxs'
DEFAULT_FROM_EMAIL = 'MyFitness <sonaraharsh791@gmail.com>'
```

### Replace with:
```python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here-change-in-production'

# Email Configuration for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Change this
EMAIL_HOST_PASSWORD = 'your-app-password'  # Change this
DEFAULT_FROM_EMAIL = 'MyFitness <your-email@gmail.com>'  # Change this
```

---

## 🎯 After Upload

Once uploaded to GitHub, add a note in README.md:

```markdown
## Configuration

1. Copy `.env.example` to `.env`
2. Update the values in `.env` with your own:
   - SECRET_KEY
   - EMAIL_HOST_USER
   - EMAIL_HOST_PASSWORD
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
```

---

## ⚠️ What Happens If You Upload Sensitive Data?

If you accidentally upload sensitive data:

1. **Change the credentials immediately**:
   - Generate new SECRET_KEY
   - Change email password
   - Revoke any API keys

2. **Remove from Git history**:
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch myproject/settings.py" \
  --prune-empty --tag-name-filter cat -- --all
```

3. **Force push**:
```bash
git push origin --force --all
```

4. **Better**: Delete the repository and create a new one with cleaned code

---

## ✅ You're Ready When:

- ✅ No real passwords in code
- ✅ No real email addresses in code
- ✅ No real SECRET_KEY in code
- ✅ .gitignore is working
- ✅ Database file won't be uploaded
- ✅ README.md is updated

**Then you can safely upload to GitHub!** 🚀
