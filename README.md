# 🌿 Wellness Assistant Chatbot

Welcome to the Wellness Assistant Chatbot project! This project leverages modern web technologies, Flask, Socket.IO, and Generative AI to create a responsive chatbot capable of providing secure, real-time health and wellness advice.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![Gemini](https://img.shields.io/badge/AI-Gemini-orange?logo=google)

## ✨ Application Features

*   Interactive User Interface: Clean, user-friendly design with a responsive layout for seamless usage on all devices.
*   Generative AI Integration: Powered by Google Generative AI (Gemini) for insightful, context-aware wellness advice.
*   Real-time Chat: Uses Flask and Socket.IO for instant response rendering without page reloads.
*   Secure Architecture: API keys are strictly managed via environment variables (.env) to prevent leakage, and chat histories are isolated per user session.
*   Easy Deployment: Modular structure for straightforward setup and deployment.

## ⚙️ How It Works

### Frontend
The user interacts with a responsive web page. User input is collected through a form and sent to the backend securely via Socket.IO. The frontend also handles dynamic rendering of the AI's response and loading states.

### Backend
*   Flask handles the initial HTTP requests and serves the frontend templates.
*   Flask-SocketIO manages persistent, real-time communication between the client and server.
*   The backend formats the user's prompt, sends it to the Google Generative AI API, retrieves the response, and forwards it back to the frontend instantly.

## 🛠️ Tech Stack

*   Frontend: HTML5, CSS3 (Custom styling for an intuitive, calming user experience).
*   Backend: Python, Flask, Flask-SocketIO.
*   AI Engine: Google Generative AI API.

## 🚀 Setup & Installation

### Prerequisites
*   Python 3.9+ installed.
*   A Google Generative AI API key (Get one at [Google AI Studio](https://aistudio.google.com/app/apikey)).

### Steps to Run Locally

1. Clone the repository:
   `bash
   git clone https://github.com/Devminimah/AI-Hackathon.git
   cd your-repo-name
