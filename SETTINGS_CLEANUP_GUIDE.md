# 🔒 Settings.py Cleanup for GitHub

## Current Sensitive Data in Your settings.py:

1. **SECRET_KEY**: `django-insecure-$jew9(s=i9!l0#hl_uhsjk8*e2=ni6qrxzghhb-%%+_)3q#+^6`
2. **EMAIL_HOST_USER**: `sonaraharsh791@gmail.com`
3. **EMAIL_HOST_PASSWORD**: `ftbcalkoivjlgvxs`

## ⚠️ IMPORTANT: Change These Before Uploading!

### Option 1: Quick Manual Fix (Easiest)

Open `myproject/settings.py` and make these changes:

#### Line 23 - Change SECRET_KEY:
```python
# BEFORE:
SECRET_KEY = 'django-insecure-$jew9(s=i9!l0#hl_uhsjk8*e2=ni6qrxzghhb-%%+_)3q#+^6'

# AFTER:
SECRET_KEY = 'your-secret-key-here-change-in-production'
```

#### Lines 152-157 - Change Email Settings:
```python
# BEFORE:
EMAIL_HOST_USER = 'sonaraharsh791@gmail.com'
EMAIL_HOST_PASSWORD = 'ftbcalkoivjlgvxs'
DEFAULT_FROM_EMAIL = 'MyFitness <sonaraharsh791@gmail.com>'

# AFTER:
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'MyFitness <your-email@gmail.com>'
```

### Option 2: Use Environment Variables (Recommended for Production)

1. **Install python-decouple**:
```bash
pip install python-decouple
```

2. **Update requirements.txt**:
Add this line:
```
python-decouple==3.8
```

3. **Create .env file** (this won't be uploaded):
```
SECRET_KEY=django-insecure-$jew9(s=i9!l0#hl_uhsjk8*e2=ni6qrxzghhb-%%+_)3q#+^6
DEBUG=True
EMAIL_HOST_USER=sonaraharsh791@gmail.com
EMAIL_HOST_PASSWORD=ftbcalkoivjlgvxs
```

4. **Update settings.py**:
```python
from decouple import config

# At line 23:
SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')

# At line 26:
DEBUG = config('DEBUG', default=False, cast=bool)

# At lines 152-157:
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = f'MyFitness <{EMAIL_HOST_USER}>'
```

---

## 📝 Step-by-Step Instructions

### For Quick Manual Fix:

1. Open `myproject/settings.py` in your editor
2. Press `Ctrl+F` to find
3. Search for: `django-insecure-$jew9`
4. Replace the entire SECRET_KEY value with: `your-secret-key-here`
5. Search for: `sonaraharsh791@gmail.com`
6. Replace with: `your-email@gmail.com`
7. Search for: `ftbcalkoivjlgvxs`
8. Replace with: `your-app-password`
9. Save the file
10. Now it's safe to upload!

---

## ✅ Verification

After making changes, check your settings.py:

```bash
# Search for sensitive data
grep -n "sonaraharsh791" myproject/settings.py
grep -n "ftbcalkoivjlgvxs" myproject/settings.py
grep -n "django-insecure-\$jew9" myproject/settings.py
```

If these commands return nothing, you're good! ✅

---

## 🎯 What Users Will Do After Cloning

Add this to your README.md:

```markdown
## Setup Instructions

1. Clone the repository
2. Create virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`
5. Update `.env` with your own values:
   - Generate new SECRET_KEY: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - Add your email credentials
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`
```

---

## 🔐 Generate New SECRET_KEY

To generate a new SECRET_KEY for production:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

This will output something like:
```
django-insecure-new-random-key-here
```

---

## ⚠️ Remember

- ✅ .gitignore already excludes `.env` file
- ✅ .gitignore already excludes `db.sqlite3`
- ✅ Your actual credentials stay on your local machine
- ✅ GitHub will only get placeholder values

---

## 🚀 Ready to Upload?

After cleaning settings.py:

```bash
# Check what will be uploaded
git status

# Add files
git add .

# Commit
git commit -m "Initial commit: MyFitness project"

# Push to GitHub
git push -u origin main
```

---

**Your sensitive data will be safe!** 🔒
