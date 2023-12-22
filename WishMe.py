
import time
import datetime
# Define function to speak text
def speak(text):
    print(f'Bot:  {text}')


hour = int(datetime.datetime.now().hour)
if 0 <= hour < 12:
    speak("Good Morning!")
elif 12 <= hour < 18:
    speak("Good Afternoon!")
else:
    speak("Good Evening!")
speak("how may I help you?")