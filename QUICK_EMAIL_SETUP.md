# Quick Email Setup - 5 Minutes ⚡

## What You Need:
- Your Gmail address
- 5 minutes

---

## Step 1: Get App Password (2 minutes)

1. Go to: https://myaccount.google.com/security
2. Enable **2-Step Verification** (if not already enabled)
3. Click **App passwords**
4. Select: **Mail** → **Other (Custom name)** → Type: "MyFitness"
5. Click **Generate**
6. **COPY the 16-character password** (e.g., `abcd efgh ijkl mnop`)

---

## Step 2: Update Settings (1 minute)

Open `myproject/settings.py` and find these lines (near the bottom):

```python
EMAIL_HOST_USER = 'your-email@gmail.com'  # ← Put YOUR Gmail here
EMAIL_HOST_PASSWORD = 'your-app-password'  # ← Put App Password here (no spaces!)
DEFAULT_FROM_EMAIL = 'MyFitness <your-email@gmail.com>'  # ← Put YOUR Gmail here
```

**Example:**
```python
EMAIL_HOST_USER = 'sonaraharsh791@gmail.com'
EMAIL_HOST_PASSWORD = 'abcdefghijklmnop'
DEFAULT_FROM_EMAIL = 'MyFitness <sonaraharsh791@gmail.com>'
```

---

## Step 3: Restart Server (30 seconds)

Stop the server (Ctrl+C) and restart:
```bash
python manage.py runserver
```

---

## Step 4: Test It! (1 minute)

1. Go to: http://127.0.0.1:8000/password-reset/
2. Enter your email (or admin email)
3. Click "Send Reset Link"
4. Check your email inbox!

---

## Done! 🎉

Password reset emails will now be sent from your Gmail!

---

## Troubleshooting

**Email not sending?**
- Check you removed spaces from App Password
- Make sure 2-Step Verification is ON
- Check spam folder
- Look at Django console for errors

**Can't find App Passwords?**
- Enable 2-Step Verification first
- Wait 5 minutes
- Refresh the page

---

## For Testing Without Email

Want to test without Gmail setup? Use console backend:

In `settings.py`, change:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Emails will print in your terminal instead!

---

**That's it! Super simple!** 🚀
