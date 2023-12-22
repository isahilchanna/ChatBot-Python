import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import AppOpener
import ctypes
import logging
# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',130)
# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(f'Bot:  {text}')

# Define function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bot:  Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)  # Adjust for ambient noise
        audio = r.listen(source, timeout=5)  # Listen for up to 5 seconds
    try:
        print("Bot:  Recognizing...")
        query = r.recognize_google(audio, language='hi-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:


        print("Bot:  Could not understand audio")
        return "None"
    except sr.RequestError as e:
        print(f"Bot:  Could not request results from Google Speech Recognition; {e}")
        return "None"
    return query
# Define function to wish user
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon! sir")
    else:
        speak("Good Evening! sir")
    speak("I am your P.A A.I powered. How may I help you?")

# Main program
if __name__ == "__main__":
    wish_me()
    while True:
        logging.info("A.I is listening")
        query = recognize_speech().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")
        elif 'search in wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search in wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'spell' in query:
            speak("Please spell the word")
            word = recognize_speech().lower()
            speak(word)
        elif 'quit' in query :
            speak("Goodbye!")
            exit()
        elif 'exit' in query or 'stop' in query :

            speak("Goodbye!")
            exit()
        elif 'bye' in query or 'mar ja' in query:
            speak("Goodbye!")
            exit()
        elif 'close 'in query:
            speak("Closing app")
            AppOpener.close((query.replace("close ", "")),match_closest=True,output=False)
        elif 'open 'in query:
            speak("Opening app")
            AppOpener.open((query.replace("open ", "")),match_closest=True,output=False)
        elif 'switch 'in query:
            speak("Switching app")
            AppOpener.switch((query.replace("switch ", "")),match_closest=True,output=False)
        elif 'minimize 'in query:
            speak("Minimizing app")
            AppOpener.minimize((query.replace("minimize ", "")),match_closest=True,output=False)
        elif 'speak' in query:
            query = query.replace("speak", "")
            speak(query)
        elif 'what is your name' in query:
            speak("My name is Jarvis")



