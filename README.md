# EduGenie 3

Google Gemini Powered Learning Assistant with a fallback response system.

## Features

- Gemini AI as the primary response engine
- Automatic fallback when Gemini is unavailable
- Flask backend
- Clean responsive chat UI
- API key stored in `.env`

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate

Windows:

```bash
venv\Scripts\activate
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini

Copy `.env.example` to `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run

```bash
python app.py
```

Open:

http://127.0.0.1:5000

If Gemini reaches its limit or fails, EduGenie automatically uses the fallback engine.
