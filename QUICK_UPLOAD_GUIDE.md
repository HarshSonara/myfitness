# ⚡ Quick Upload Guide for Harsh

## 🎯 3 Simple Steps

### 1️⃣ Clean Settings (2 minutes)

Open `myproject/settings.py`:

**Find line 23, change to:**
```python
SECRET_KEY = 'your-secret-key-here'
```

**Find line 156-157, change to:**
```python
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

**Save the file!**

---

### 2️⃣ Create GitHub Repo (1 minute)

1. Go to: https://github.com/new
2. Name: `myfitness`
3. Click "Create repository"

---

### 3️⃣ Upload (2 minutes)

Copy-paste these commands in terminal:

```bash
git init
git add .
git commit -m "Initial commit: MyFitness Django project"
git remote add origin https://github.com/HarshSonara/myfitness.git
git branch -M main
git push -u origin main
```

**Username**: HarshSonara  
**Password**: Your Personal Access Token

Get token: https://github.com/settings/tokens

---

## ✅ Done!

Your project will be at:
**https://github.com/HarshSonara/myfitness**

---

## 📚 Detailed Guides Available:

- `UPLOAD_COMMANDS_FOR_HARSH.md` - Personalized for you
- `UPLOAD_TO_GITHUB_COMPLETE.md` - Complete guide
- `SETTINGS_CLEANUP_GUIDE.md` - Security details
- `upload_to_github.txt` - Commands only

---

**Total Time: 5 minutes** ⏱️
