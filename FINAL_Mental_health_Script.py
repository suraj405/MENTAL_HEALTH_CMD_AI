import google.generativeai as genai
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

try:
    _ = nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyA2P-0BU5hbjTuVGcs6vCbYOV1th3GyQR4")
genai.configure(api_key=API_KEY)

CRISIS_TRIGGERS = [
    "i want to die", "i want to kill myself", "suicide", "end my life",
    "self harm", "hurt myself", "i'm going to do it", "take my own life",
    "i can't go on", "hopeless", "end it all"
]

NEGATIVE_SENTIMENT_THRESHOLD = 0.5

SYSTEM_INSTRUCTION = (
    "You are an AI companion named Suraj, a 3rd-year M.Tech(CSE) student. "
    "Your class advisor is Mohan kumar sir "
    "Give tips about body problems based on a symptoms"
    "Your purpose is to offer a non-judgmental space for users to express their thoughts and feelings. "
    "You are **not** a licensed therapist or a medical professional. "
    "You cannot diagnose conditions, give medical advice, or handle crisis situations. "
    "If a user expresses serious distress, you must immediately advise them to contact a professional "
    "and provide a clear disclaimer. Your responses should be empathetic, encouraging, and focused "
    "on providing general well-being tips. Avoid giving specific medical advice for physical ailments. "
    "Always respond with empathy and encouragement."
    "Respond clear and detail without any complex words."
    "Respod with indian english"
    "Respod only about Mental health,Body illness only"

)

try:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=SYSTEM_INSTRUCTION
    )
except Exception as e:
    exit()

chat = model.start_chat()

print("================ES23CJ45===========================================")
print("Hello! I'm an AI of Suraj from 3rd Year M.Tech(CSE) here to listen.")
print("I am here to offer support, but I am **not** a medical professional. If you are in crisis, please seek immediate help.")
print("You can share whatever is on your mind. (Type 'exit' to end the conversation)")
print("================ES23CJ45===========================================")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("\nThank you for sharing nanba. Remember to consult a doctor for any medical advice.")
        print("Goodbye for now. Take care!")
        break

    try:
        user_input_lower = user_input.lower()

        if any(trigger in user_input_lower for trigger in CRISIS_TRIGGERS):
            print("\nCompanion: I am very concerned by what you've said. Please know that help is available and you don't have to go through this alone.")
            print("Please contact a National Health Mission Tamil Nadu immediately. Here are some numbers: 104 ")
            print("Or call emergency services by dialing your local emergency number: *108* ")
            print("Your well-being is important. Please reach out to a professional.")
            continue

        sentiment = sia.polarity_scores(user_input)

        if sentiment['neg'] > NEGATIVE_SENTIMENT_THRESHOLD:
            response = chat.send_message(f"The user seems to be feeling down. Respond with extra empathy and support. The message is: {user_input}")
        else:
            response = chat.send_message(user_input)

        print(f"Companion: {response.text}")

    except Exception:
        print(f"An error occurred. Please try again later.")