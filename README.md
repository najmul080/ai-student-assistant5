# AI Student Assistant — Render Assignment

This is a very simple Flask web service for the assignment:

**"Make a simple Render-based cloud service that uses AI feature."**

## Features
- Home page
- Student name and student ID
- Working AI feature
- Gemini API integration
- Ready for Render deployment

## 1. Change your details

Open `app.py` and change:

```python
STUDENT_NAME = "Islam MD Najmul"
STUDENT_ID = "YOUR_STUDENT_ID"
```

Put your real student ID in `STUDENT_ID`.

## 2. Create Gemini API key

Go to Google AI Studio and create an API key.

Do NOT put the key inside `app.py` and do NOT upload it to GitHub.

## 3. Upload this project to GitHub

Create a new GitHub repository and upload all files/folders from this project.

## 4. Deploy to Render

Create a new **Web Service** and connect the GitHub repository.

Use:

Build Command:
```text
pip install -r requirements.txt
```

Start Command:
```text
gunicorn app:app
```

Choose the Free plan if it is available for your account.

## 5. Add API key in Render

Render Dashboard → your service → Environment → Add Environment Variable

Key:
```text
GEMINI_API_KEY
```

Value:
```text
YOUR_GEMINI_API_KEY
```

Save and redeploy.

## 6. Test

Open your Render `onrender.com` URL.

Type:
```text
Explain artificial intelligence in simple words.
```

Click **Ask AI**.

If an answer appears, the AI cloud service is working.

## Presentation

Explain:

1. I created a Flask web application.
2. I deployed it as a Web Service on Render.
3. The website contains my name and student ID.
4. The website sends a question to the backend.
5. The backend calls the Gemini API.
6. Gemini returns an AI-generated answer.
7. The answer is displayed on the website.

## Important

Keep the API key private. Store it in Render Environment Variables, not in GitHub source code.
