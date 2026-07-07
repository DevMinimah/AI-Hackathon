# mainchatbackend.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Securely fetch the API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("🚨 ERROR: GEMINI_API_KEY not found in your .env file!")

# 3. Configure the model
genai.configure(api_key=API_KEY)
# Note: Google updates model names frequently. If "gemini-pro" throws an error, 
# try "gemini-1.5-flash" or "gemini-1.5-pro".
model = genai.GenerativeModel("gemini-pro")

def custom_gemini_chat(user_input, history):
    """Interacts with the Gemini model to get a response."""
    prompt = f"""You are a medical expert specializing in wellness and health improvement. 
    Please provide a helpful and informative response to the following query, 
    taking into account the previous conversation:

    {''.join([f'User: {u}\nAI: {a}\n' for u, a in history])}
    User: {user_input}"""

    try:
        response = model.generate_content(prompt)
        # Safety check: Ensure the model actually returned text
        if not response.text:
            return "I cannot answer that due to safety guidelines. Please try a different question."
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while talking to the AI: {e}"

if __name__ == "__main__":
    print("🌿 Welcome to Your Wellness Assistant (Local Testing Mode)!")
    print("Type 'quit' or 'exit' to stop.\n" + "-"*40)
    
    history = []  

    while True:
        user_input = input("\n🧑 You: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! Stay healthy.")
            break
            
        if not user_input.strip():
            continue

        reply = custom_gemini_chat(user_input, history)
        history.append((user_input, reply))
        
        print("\n🤖 AI:")
        print(reply)