import os
import google.generativeai as genai
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Secure API key loading
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Per-user chat history (keyed by SocketIO session ID)
client_histories = {}

SYSTEM_PROMPT = """
You are a knowledgeable wellness and health improvement assistant. 
Provide helpful, evidence-based, and empathetic responses. 
ALWAYS include a disclaimer that you are an AI and not a substitute for professional medical advice, diagnosis, or treatment.
"""

def get_ai_response(user_input: str, history: list) -> str:
    """Safely call Gemini with proper error handling."""
    # Format history for Gemini's expected structure
    formatted_history = [{"role": "user" if i % 2 == 0 else "model", "parts": [msg]} 
                         for i, msg in enumerate([h for pair in history for h in pair])]
    
    chat = model.start_chat(history=formatted_history)
    
    try:
        response = chat.send_message(user_input)
        if not response.text:
            return "I'm unable to answer that due to safety guidelines. Please rephrase or ask another wellness question."
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "The AI service is temporarily unavailable. Please try again shortly."

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(message):
    sid = request.sid
    if sid not in client_histories:
        client_histories[sid] = []
    
    # Optional: basic input validation
    if not message or len(message.strip()) == 0:
        emit("response", "Please enter a valid question.")
        return

    try:
        ai_reply = get_ai_response(message.strip(), client_histories[sid])
        client_histories[sid].append((message.strip(), ai_reply))
        
        # Keep history manageable (last 10 turns)
        if len(client_histories[sid]) > 10:
            client_histories[sid] = client_histories[sid][-10:]
            
        emit("response", ai_reply)
    except Exception as e:
        emit("response", "An unexpected error occurred. Please try again later.")

@socketio.on("disconnect")
def handle_disconnect():
    sid = request.sid
    client_histories.pop(sid, None)

if __name__ == '__main__':
    # Use production server (e.g., gunicorn + eventlet) for deployment
    socketio.run(app, debug=False, allow_unsafe_werkzeug=True)