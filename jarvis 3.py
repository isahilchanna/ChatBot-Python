
from encodings import search_function
import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init()

voice = engine.getProperty('voices')
newVoiceRate = 200
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voices', voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date  = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("you are  back sir!!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <=12:
        speak("Good Morning sir!!")
    elif hour >=12 and hour <= 18 :
        speak("Good Afternoon sir!!")
    elif hour >=18 and hour<= 24:
        speak("Good Evening sir!!")
    else:
        speak("Good Night sir!! have a sweet dream!")
        speak("GST sir !! good night , sweet dreams , take care!! bye")
    
    speak("lucifier at your service! how can i help you my lord?")

def takeCommand():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir!...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing your command sir!!...")
        query = r.recognize_google(audio, "en =US")
        print(query)
    except Exception as e:
        print (e)
        speak("Sir please say that again please...")

        return "None"
    return query
if __name__ == "__main__":
    
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "quit" in query or "offline" in query or "switch off" in query:
            speak("On your command sir!!")
            speak("Going offline sir in 3 2 1 good bye sir....")
            quit()

        

