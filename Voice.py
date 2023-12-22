import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Define function to speak text
def speak(text):
    print(f'Bot:  {text}')
    engine.say(text)
    engine.runAndWait()


speak("Hello, I am your Personalised AI ChatBot. How may I help you?")