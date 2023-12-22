import PIL.Image
import pystray
from PIL import Image


import pyttsx3
from subprocess import call


image = PIL.Image.open("infinity.png")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def if_clicked(icon, item):
    if str(item) == 'Yes':
        speak("So i guess we are starttighten your seatbelts! we are ready to launch!!")
        print("So i guess we are going to start on, tighten your seatbelts! \nWe are ready to launch!!")
        print("Starting!!")
        speak("Starting")
        speak("Started!")
        call(["python", "Personalised AI ChatBot.py"])
    elif str(item) == 'No':

        speak("So you dont want me to start yet? that\'s totally okay. tell me when you are ready")
        print("So you dont want me to start yet? \n that\'s totally okay. tell me, when you are ready")


    elif str(item) == "Stop":
        speak("Au revoir , see you soon!")
        print("Au revoir , see you soon!")
        icon.stop()


icon = pystray.Icon("Infinity", image, menu=pystray.Menu(
    pystray.MenuItem("Start", pystray.Menu(
        pystray.MenuItem("Yes", if_clicked),
        pystray.MenuItem("No", if_clicked)
    )),
    pystray.MenuItem("Stop", if_clicked),
))
if __name__ == '__main__':
    icon.run()
