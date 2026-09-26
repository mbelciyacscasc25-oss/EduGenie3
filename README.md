# 🎓 EduGenie3 — AI-Powered Learning Assistant

> An AI-powered learning assistant designed to help students learn concepts, practice quizzes, and track their learning progress.

## 🚀 Live Demo

### 🌐 Try EduGenie3 Online

👉 **[Open EduGenie3 Live Demo](https://edugenie3.onrender.com)**

**Live Application:**  
https://edugenie3.onrender.com

---

## 📌 About The Project

**EduGenie3** is a web-based AI-powered learning assistant developed to provide students with an interactive and personalized learning experience.

The application combines **Google Gemini AI** with a **fallback response system** to provide learning assistance while maintaining basic functionality even when the Gemini API is temporarily unavailable.

EduGenie3 provides students with:

- 🤖 AI-powered learning assistance
- 📚 Subject-based learning
- 🧠 Interactive quizzes
- 📊 Learning progress tracking
- 🔄 AI fallback support
- 🎨 Modern and responsive user interface

---

## ✨ Features

### 🤖 AI Learning Assistant

Students can ask questions and receive AI-generated explanations using Google Gemini.

**Features:**

- Ask academic questions
- Get AI-generated explanations
- Student-friendly responses
- Interactive learning support

---

### 🔄 AI Fallback System

EduGenie3 includes a fallback mechanism to maintain application functionality when Gemini is unavailable.

```text
                    User Question
                         │
                         ▼
                  Gemini AI Available?
                    /           \
                  YES             NO
                   │               │
                   ▼               ▼
             Gemini Response   Fallback System
                   │               │
                   └───────┬───────┘
                           ▼
                     Student Response