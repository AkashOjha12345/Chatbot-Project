import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("🧑 You said:", text)
        return text.lower()
    except:
        return ""

# ---------------------------
# CHATBOT LOGIC (PASTE HERE)
# ---------------------------
user_name = ""

def chatbot_reply(user_text):
    global user_name

    if "my name is" in user_text:
        user_name = user_text.replace("my name is", "").strip()
        return f"Nice to meet you, {user_name}"

    elif "hello" in user_text:
        if user_name:
            return f"Hello {user_name}! How can I help you?"
        return "Hello! How can I help you?"

    elif "your name" in user_text:
        return "I am your AI voice assistant."

    elif "how are you" in user_text:
        return "I am doing great. Thank you!"

    elif "what is my name" in user_text:
        if user_name:
            return f"Your name is {user_name}"
        else:
            return "I don't know your name yet. Please tell me."

    elif "bye" in user_text or "exit" in user_text:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I did not understand that."

# ---------------------------
# MAIN PROGRAM
# ---------------------------
speak("Hello! I am your voice chatbot. You can speak now.")

while True:
    user_input = listen()
    if user_input == "":
        continue

    response = chatbot_reply(user_input)
    print("🤖 AI:", response)
    speak(response)

    if "bye" in user_input or "exit" in user_input:
        break
