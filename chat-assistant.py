# Project 2 – AI Study Buddy (Rule-Based Chat Assistant in Python)

import datetime
import time

name = input("Enter your name: ")
# Time based greeting
hour = datetime.datetime.now().hour

if 5 <= hour <= 12:
    print ("Good Morning!",name)
elif 12 <= hour < 17: 
    print ("Good Afternoon!",name)
elif 17 <= hour <= 21:
    print ("Good Evening!",name)
else:
    print ("Good Night!",name)

print ("\nHello! Welcome to your Chatbot",name)
print ("You can talk to me. Type 'bye' anytime to exit\n")

# Chatbot memory creation [ dictionary of responses ]
responses = {
    "hello" : "Hi there! How can I help you.?",
    "how are you" : "I'm very fine. Thankyou",
    "who are you" : "I'm your friendly AI Study Buddy",
    "motivate me" : f"Keep going,{name}. Every bug of your project makes you a better developer",
    "happy" : "That's great to hear! Keep that positive energy going",
    "sad" : f"Don't worry,{name}! Even code breaks sometimes, but it always runs again",
    "tell me about python" : "Python is powerful — it can do AI, automation, and much more!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "weather" : "I can't check weather yet, but I'm learning!",
    "made by" : "I was created by Hajira as part of her Python learning journey!",
    "help" : "I can talk about: hello, time, motivation, python, jokes, and more!",
    "bye" : f"Goodbye,{name}! Keep learning and exploring"
}

# Method/Function to get response of Chatbot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I'm not able to tell that yet. I'll learn it soon"

while True:
# User Input
    userInput = input("Your question: ")
    reply = getResponseOfBot(userInput)
    time.sleep(1)  # Slight delay for realistic feel
    print ("Bot response : ", reply)

    if "bye" in userInput.lower():
        break