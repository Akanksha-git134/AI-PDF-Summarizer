# 🤖 AI PDF Summarizer

An AI-powered Flask web application that summarizes PDF documents using Google's Gemini AI.

## Features

- Upload PDF files
- AI-generated reports
- Page and word count
- Dark Mode
- Multiple Gemini API Key Support
- Responsive UI

## Technologies

- Python
- Flask
- Gemini API
- HTML
- CSS
- JavaScript

## Getting Started (Local Setup)

### 1. Clone the repo
```bash
git clone https://github.com/Akanksha-git134/AI-PDF-Summarizer.git
cd AI-PDF-Summarizer
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Copy `.env.example` to a new file named `.env`:
```bash
cp .env.example .env
```
Then open `.env` and add at least one free Gemini API key (get one at [aistudio.google.com/apikey](https://aistudio.google.com/apikey)):
```
GEMINI_API_KEY_1=your_api_key_here
GEMINI_API_KEY_2=your_api_key_here
GEMINI_API_KEY_3=your_api_key_here
```
Only `GEMINI_API_KEY_1` is required — keys 2 and 3 are optional fallbacks the app tries automatically if the first key hits its rate limit.

### 5. Run the app
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000`.

## Deploying on Render

1. Push this repo to your own GitHub account.
2. On [Render](https://render.com), click **New > Web Service** and connect the repo.
3. Use these settings:
   | Setting | Value |
   |---|---|
   | Build Command | `pip install -r requirements.txt` |
   | Start Command | `gunicorn app:app` |
4. Under **Environment**, add the same variables from your `.env` file:
   - `GEMINI_API_KEY_1` (required)
   - `GEMINI_API_KEY_2`, `GEMINI_API_KEY_3` (optional)
5. Deploy. Render will rebuild automatically on every push to your linked branch.

> **Note:** never commit your real `.env` file — it's already excluded via `.gitignore`. Only `.env.example` (with placeholder values) should be in the repo.

# PREVIEW

<img width="1907" height="903" alt="image" src="https://github.com/user-attachments/assets/db283a74-fbbb-4ef6-b142-95df1f4d8ae8" />

<img width="1872" height="892" alt="image" src="https://github.com/user-attachments/assets/99a504fa-0994-48fb-a3f8-3b46ea4ce332" />

<img width="1885" height="898" alt="image" src="https://github.com/user-attachments/assets/cff79fcd-f10c-46a6-83ac-bc8dd9ded2ce" />

<img width="1872" height="917" alt="image" src="https://github.com/user-attachments/assets/d6990e4e-edf0-40f0-bb89-ba58acd415fa" />

