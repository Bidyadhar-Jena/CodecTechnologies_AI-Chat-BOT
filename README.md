# 🤖 AI-Powered Chatbot

An AI-Powered Chatbot developed using Python and Flask that provides an interactive web-based interface for users to communicate with a chatbot.

The project is designed as a practical application of Python programming, web development, chatbot logic, environment-variable management, and software testing.

---

## 📌 About the Project

The AI-Powered Chatbot is a web-based chatbot application built with Python and Flask.

It provides users with a simple and interactive interface where they can enter messages and receive responses from the chatbot.

The project separates the web application from the chatbot processing logic, making the code easier to understand, maintain, and extend.

This project was developed as part of an internship project with **Codec Technologies**.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To develop a functional chatbot using Python.
- To create a web interface using Flask.
- To implement chatbot response processing separately from the web application.
- To understand client-server communication.
- To manage API keys securely using environment variables.
- To organize a Python project using a modular structure.
- To implement basic automated testing.
- To provide a foundation that can be extended with advanced AI and NLP capabilities.

---

## ✨ Features

### 💬 Interactive Chat

Users can enter messages through the web interface and communicate with the chatbot.

### 🌐 Flask Web Application

The application uses Flask to create the backend web server and handle user requests.

### 🧠 Chatbot Engine

The chatbot processing logic is separated into `chatbot_engine.py`.

This makes it easier to modify or extend the chatbot without changing the main Flask application.

### 🎨 Web Interface

The frontend uses:

- HTML
- CSS
- JavaScript

to provide a simple chat interface.

### 🔐 Environment Variable Support

API credentials can be stored using environment variables instead of hardcoding sensitive information inside Python source files.

### 🧪 Automated Testing

Basic chatbot functionality can be tested using Python testing tools.

### 📁 Modular Project Structure

The project is organized into separate folders for application code, frontend files, tests, and documentation.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| HTML5 | Web page structure |
| CSS3 | Web page styling |
| JavaScript | Frontend interaction |
| python-dotenv | Environment variable management |
| Pytest | Automated testing |

---

## 📂 Project Structure

CodecTechnologies_AI-Chat-BOT/
│
├── chatbot/
│   ├── __init__.py
│   ├── app.py
│   ├── chatbot_engine.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── style.css
│       └── chat.js
│
├── tests/
│   └── test_chatbot.py
│
├── docs/
│   └── CHATBOT_SETUP.md
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
│
└── LICENSE text

## Author 
Bidyadhar Jena
