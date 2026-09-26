# 🎓 EduGenie3 — AI-Powered Learning Assistant

> An AI-powered learning assistant designed to help students learn concepts, practice quizzes, and track their learning progress.

---

## 🚀 Live Demo

### 🌐 Try EduGenie3 Online

👉 **[Open EduGenie3 Live Demo](https://edugenie3.onrender.com)**

**Live Application:**  
https://edugenie3.onrender.com

---

## 📌 About The Project

**EduGenie3** is a web-based AI-powered learning assistant developed to provide students with an interactive and personalized learning experience.

The application integrates **Google Gemini AI** with a **fallback response system**, allowing the application to continue providing useful learning support when the Gemini API is unavailable or reaches its usage limit.

EduGenie3 brings multiple learning features together in one platform, including AI assistance, subject learning, interactive quizzes, and progress tracking.

---

## ✨ Features

### 🤖 AI Learning Assistant

Students can ask academic questions and receive AI-generated explanations using Google Gemini.

**Features:**

- Ask questions about academic topics
- Get AI-generated explanations
- Simple and student-friendly responses
- Gemini-powered learning support
- Interactive learning assistance

---

### 🔄 AI Fallback System

EduGenie3 includes a fallback mechanism to maintain basic learning assistance when the Gemini API is unavailable.

**Features:**

- Automatically handles Gemini API unavailability
- Uses predefined fallback responses
- Reduces dependency on continuous API availability
- Maintains application functionality during API limitations

Fallback responses are stored in:

```text
data/fallback_responses.json

📁 Project Structure
EduGenie3/
│
├── ai/
│   ├── __init__.py
│   ├── fallback.py
│   └── gemini.py
│
├── data/
│   └── fallback_responses.json
│
├── static/
│   ├── css/
│   │   ├── dashboard.css
│   │   ├── progress.css
│   │   ├── quiz.css
│   │   ├── style.css
│   │   └── subjects.css
│   │
│   └── js/
│       ├── app.js
│       ├── progress.js
│       └── quiz.js
│
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   ├── progress.html
│   ├── quiz.html
│   └── subjects.html
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

📚 Subject Learning

Students can explore subjects through a dedicated learning interface.

Includes:

Subject-based learning
Organized learning content
Easy navigation
Student-friendly interface
🧠 Interactive Quiz

EduGenie3 provides an interactive quiz module for practice and self-assessment.

Features:

Multiple-choice questions
Interactive quiz interface
Score calculation
Quiz result display
Practice-based learning
📊 Progress Tracking

Students can monitor their learning progress through the progress section.

Includes:

Learning progress
Quiz performance
Completed activities
Progress visualization
🎨 Modern Student Dashboard

The application provides a clean and responsive student interface.

Features:

Modern design
Responsive layout
Easy navigation
Student-focused interface
Mobile-friendly design
🛠️ Technologies Used
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
Artificial Intelligence
Google Gemini API
Google GenAI SDK
Fallback AI Response System
Data
JSON
Configuration
Python-dotenv
Environment Variables
Deployment
Render
Gunicorn
Development & Version Control
Visual Studio Code
Python Virtual Environment
Git
GitHub

▶️ Run the Application Locally

After activating the virtual environment:
python app.py

The application will normally be available at:
http://127.0.0.1:5000

Open the URL in your browser.