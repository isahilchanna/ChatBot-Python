import time
from winotify import Notification, audio

def Drink_Water():
    toast = Notification(app_id="Lucifier",
                         title='drink water',
                         msg="Drink WATer",
                         duration="long",
                         icon=r'D:\Languages\PYTHON\python programs\Jarvis\Jarvis {Text_Version_1,0}\icon.ico')

    toast.set_audio(audio.SMS, loop=False)
    toast.show()


if __name__ =='__main__':

    while True:
        current_time = time.strftime("%I:%M %p")

        if current_time.endswith(":00 AM") or current_time.endswith(":00 PM"):
            Drink_Water()
# Drink_Water()