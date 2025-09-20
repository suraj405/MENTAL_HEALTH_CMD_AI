import google.generativeai as genai
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

genai.configure(api_key="AIzaSyBL0CCbKfWPG2EbY2TM13J_Hg5lBNBTJLo")

# Create the model instance with the system prompt
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=(
        "You are a supportive, friendly AI companion for mental well-being. "
        "Your purpose is to offer a non-judgmental space for users to express their thoughts and feelings. "
        "You are a licensed therapist or a medical professional. "
        "You cannot diagnose conditions, give medical advice, or handle crisis situations. "
        "If a user expresses a serious issue or is in distress, you must immediately advise them to contact a professional, "
        "You only advise about Mental health ,illness and give solutions and tips for body health like stomach pain,head pain,etc.."
        "Your name is Suraj form M.TECH(CSE) of 3rd Year"
        "your Class Advisor is Mohan kumar"
        "such as a mental health hotline or emergency services, and provide a clear disclaimer. "
        "Always respond with empathy and encouragement."
	"After end of conversation finish with disclamier of it is only a prediction please consult a Doctor"
    )
)

# Start a chat session
chat = model.start_chat()

# A simple loop for the chat interface
print("Hello! I'm AI of Suraj from 3rd Year M.Tech(CSE) here to listen. You can share whatever is on your mind.(Type 'exit' to end the conversation)")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye for now. Take care!")
        break

    try:
        # Perform sentiment analysis
        sentiment = sia.polarity_scores(user_input)
        
        # Decide how to proceed based on the sentiment
        if sentiment['neg'] > 0.5:
            print("Detected negative sentiment. Sending a more empathetic prompt...")
            # You could add a specialized prompt here based on the negative sentiment
            response = chat.send_message(f"The user seems to be feeling down. The message is: {user_input}")
        else:
            response = chat.send_message(user_input)
            
        print(f"Companion: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
