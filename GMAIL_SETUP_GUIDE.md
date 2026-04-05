# Gmail Setup Guide for Password Reset Emails 📧

## Step-by-Step Instructions

### Step 1: Enable 2-Step Verification on Your Gmail Account

1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** in the left sidebar
3. Scroll down to "How you sign in to Google"
4. Click on **2-Step Verification**
5. Follow the prompts to enable it (you'll need your phone)

---

### Step 2: Generate App Password

1. After enabling 2-Step Verification, go back to **Security**
2. Scroll down to "How you sign in to Google"
3. Click on **App passwords** (you'll see this option only after enabling 2-Step Verification)
4. You may need to sign in again
5. In the "Select app" dropdown, choose **Mail**
6. In the "Select device" dropdown, choose **Other (Custom name)**
7. Type: **MyFitness Django App**
8. Click **Generate**
9. Google will show you a 16-character password like: `abcd efgh ijkl mnop`
10. **COPY THIS PASSWORD** - you won't see it again!

---

### Step 3: Update Django Settings

Open `myproject/settings.py` and update these lines:

```python
# Email Configuration for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # ← Replace with YOUR Gmail
EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'  # ← Replace with YOUR App Password (remove spaces)
DEFAULT_FROM_EMAIL = 'MyFitness <your-email@gmail.com>'  # ← Replace with YOUR Gmail
```

**Example:**
```python
EMAIL_HOST_USER = 'harsh.fitness@gmail.com'
EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'  # No spaces!
DEFAULT_FROM_EMAIL = 'MyFitness <harsh.fitness@gmail.com>'
```

---

### Step 4: Test Email Sending

1. Restart your Django server:
   ```bash
   python manage.py runserver
   ```

2. Go to: http://127.0.0.1:8000/password-reset/

3. Enter a user's email address (make sure the user has a valid email in the database)

4. Click "Send Reset Link"

5. Check the email inbox - you should receive the password reset email!

---

## Troubleshooting

### Problem: "SMTPAuthenticationError"
**Solution**: 
- Make sure you're using the App Password, NOT your regular Gmail password
- Remove any spaces from the App Password
- Make sure 2-Step Verification is enabled

### Problem: "SMTPException: STARTTLS extension not supported"
**Solution**:
- Make sure `EMAIL_USE_TLS = True`
- Make sure `EMAIL_PORT = 587`

### Problem: Email not received
**Solution**:
- Check spam/junk folder
- Make sure the user's email in database is correct
- Check Django console for error messages
- Try sending a test email from Gmail to verify account works

### Problem: "App passwords" option not showing
**Solution**:
- Make sure 2-Step Verification is enabled first
- Wait a few minutes after enabling 2-Step Verification
- Try signing out and back in to Google Account

---

## Security Best Practices

### 1. Use Environment Variables (Recommended for Production)

Instead of hardcoding credentials, use environment variables:

**Install python-decouple:**
```bash
pip install python-decouple
```

**Create `.env` file in project root:**
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

**Update settings.py:**
```python
from decouple import config

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = f'MyFitness <{EMAIL_HOST_USER}>'
```

**Add `.env` to `.gitignore`:**
```
.env
```

### 2. Never Commit Passwords to Git

Make sure your `.gitignore` includes:
```
.env
*.pyc
__pycache__/
db.sqlite3
```

---

## Testing Without Real Email (Development)

If you want to test without setting up Gmail, Django can print emails to console:

**In settings.py:**
```python
# For development - prints emails to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This will print the email content in your terminal instead of sending it.

---

## Email Template Customization

The current email is plain text. To make it prettier, you can create an HTML email:

**In views.py:**
```python
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create HTML email
html_content = f'''
<html>
<body style="font-family: Arial, sans-serif; padding: 20px;">
    <h2 style="color: #667eea;">Password Reset - MyFitness</h2>
    <p>Hello {user.username},</p>
    <p>You requested to reset your password.</p>
    <a href="{reset_link}" 
       style="background: linear-gradient(135deg, #667eea, #764ba2); 
              color: white; 
              padding: 15px 30px; 
              text-decoration: none; 
              border-radius: 10px; 
              display: inline-block;">
        Reset Password
    </a>
    <p>If you didn't request this, please ignore this email.</p>
    <p>Best regards,<br>MyFitness Team</p>
</body>
</html>
'''

email = EmailMultiAlternatives(
    subject,
    message,  # Plain text version
    settings.DEFAULT_FROM_EMAIL,
    [email]
)
email.attach_alternative(html_content, "text/html")
email.send()
```

---

## Quick Setup Checklist

- [ ] Enable 2-Step Verification on Gmail
- [ ] Generate App Password
- [ ] Copy App Password (remove spaces)
- [ ] Update `EMAIL_HOST_USER` in settings.py
- [ ] Update `EMAIL_HOST_PASSWORD` in settings.py
- [ ] Update `DEFAULT_FROM_EMAIL` in settings.py
- [ ] Restart Django server
- [ ] Test password reset
- [ ] Check email inbox
- [ ] Success! 🎉

---

## Current Configuration

Your Django app is now configured to:
1. Send password reset emails via Gmail
2. Use secure SMTP connection (TLS)
3. Send from your Gmail address
4. Include reset link in email
5. Handle email failures gracefully

---

## Need Help?

If you're stuck, check:
1. Django console for error messages
2. Gmail security settings
3. Make sure user has valid email in database
4. Try console backend first for testing

---

**Status**: Email configuration ready! Just add your Gmail credentials and you're good to go! 📧✨
