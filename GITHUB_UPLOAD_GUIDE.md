# 📤 How to Upload MyFitness to GitHub

## Step-by-Step Guide

### Prerequisites
- GitHub account (create one at https://github.com if you don't have)
- Git installed on your computer

### Step 1: Check Git Installation

Open your terminal and run:
```bash
git --version
```

If Git is not installed, download from: https://git-scm.com/downloads

### Step 2: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### Step 3: Create a New Repository on GitHub

1. Go to https://github.com
2. Click the "+" icon in top right
3. Select "New repository"
4. Fill in:
   - Repository name: `myfitness` (or any name you prefer)
   - Description: "Fitness & Diet Management System"
   - Choose: Public or Private
   - DO NOT initialize with README (we already have one)
5. Click "Create repository"

### Step 4: Initialize Git in Your Project

Open terminal in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files to staging
git add .

# Create first commit
git commit -m "Initial commit: MyFitness Django project"
```

### Step 5: Connect to GitHub

Replace `YOUR_USERNAME` and `REPOSITORY_NAME` with your actual GitHub username and repository name:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
```

Example:
```bash
git remote add origin https://github.com/harshsonara/myfitness.git
```

### Step 6: Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

You'll be asked for your GitHub credentials:
- Username: Your GitHub username
- Password: Your GitHub Personal Access Token (not your account password)

### Step 7: Create Personal Access Token (If Needed)

If you don't have a Personal Access Token:

1. Go to GitHub Settings
2. Click "Developer settings" (bottom left)
3. Click "Personal access tokens" → "Tokens (classic)"
4. Click "Generate new token" → "Generate new token (classic)"
5. Give it a name: "MyFitness Upload"
6. Select scopes: Check "repo" (full control of private repositories)
7. Click "Generate token"
8. COPY THE TOKEN (you won't see it again!)
9. Use this token as your password when pushing

### Step 8: Verify Upload

1. Go to your GitHub repository URL
2. You should see all your files uploaded
3. README.md will be displayed on the main page

---

## 🚀 Quick Commands (All in One)

If you want to do everything at once, copy and paste these commands:

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: MyFitness Django project"

# Add remote (REPLACE WITH YOUR URL)
git remote add origin https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## 📝 Files Prepared for GitHub

I've created these files for you:

1. **README.md** - Project documentation
2. **.gitignore** - Files to exclude from Git
3. **requirements.txt** - Python dependencies

### What's Excluded (.gitignore):
- ❌ `db.sqlite3` (database file)
- ❌ `__pycache__/` (Python cache)
- ❌ `/media` (user uploads)
- ❌ `/staticfiles` (collected static files)
- ❌ `.env` (environment variables)
- ❌ IDE files (.vscode, .idea)

### What's Included:
- ✅ All Python code (.py files)
- ✅ All templates (.html files)
- ✅ All static files (CSS, JS, images)
- ✅ Configuration files
- ✅ Documentation files

---

## ⚠️ Important Notes

### Before Pushing:

1. **Remove Sensitive Data**:
   - Open `myproject/settings.py`
   - Change `SECRET_KEY` to a placeholder:
     ```python
     SECRET_KEY = 'your-secret-key-here'
     ```
   - Remove or comment out email credentials:
     ```python
     # EMAIL_HOST_USER = 'your-email@gmail.com'
     # EMAIL_HOST_PASSWORD = 'your-app-password'
     ```

2. **Add Environment Variables Note**:
   - Create a `.env.example` file with placeholders
   - Users can copy it to `.env` and add their own values

### After Pushing:

1. **Update Repository Settings**:
   - Add topics/tags: django, python, fitness, web-app
   - Add description
   - Add website URL (if deployed)

2. **Create Releases**:
   - Go to "Releases" tab
   - Click "Create a new release"
   - Tag: v1.0.0
   - Title: "Initial Release"

---

## 🔄 Future Updates

When you make changes to your project:

```bash
# Check status
git status

# Add changed files
git add .

# Commit with message
git commit -m "Description of changes"

# Push to GitHub
git push
```

---

## 🆘 Troubleshooting

### Error: "fatal: not a git repository"
**Solution**: Run `git init` first

### Error: "remote origin already exists"
**Solution**: Run `git remote remove origin` then add again

### Error: "failed to push"
**Solution**: Run `git pull origin main --rebase` then `git push`

### Error: "Authentication failed"
**Solution**: Use Personal Access Token instead of password

### Large files error
**Solution**: Files over 100MB need Git LFS. Remove large files or use Git LFS.

---

## 📞 Need Help?

If you encounter any issues:
1. Check the error message carefully
2. Google the error message
3. Ask on Stack Overflow
4. Check GitHub documentation

---

## ✅ Checklist

Before uploading:
- [ ] Git is installed
- [ ] GitHub account created
- [ ] New repository created on GitHub
- [ ] Sensitive data removed from settings.py
- [ ] All files are ready

During upload:
- [ ] Git initialized (`git init`)
- [ ] Files added (`git add .`)
- [ ] First commit created
- [ ] Remote added
- [ ] Pushed to GitHub

After upload:
- [ ] Verify files on GitHub
- [ ] Check README displays correctly
- [ ] Add repository description
- [ ] Add topics/tags
- [ ] Share repository URL

---

**Your repository will be at**: `https://github.com/YOUR_USERNAME/REPOSITORY_NAME`

Good luck! 🚀
