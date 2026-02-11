import random
import os

responses = {
    "hi": ["Hello!", "Hi there!", "Hey 👋"],
    "how are you": ["I'm fine 😊", "Doing great!", "All good!"],
    "your name": ["I am an AI Chatbot 🤖"],
    "bye": ["Goodbye!", "See you soon 👋"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that 😅"

