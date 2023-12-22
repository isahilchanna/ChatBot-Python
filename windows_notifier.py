# from win10toast import ToastNotifier
#
# notifier= ToastNotifier()
#
# notifier.show_toast("Hii","Hey",duration=4)
import time
from winotify import Notification, audio
toast = Notification(app_id="Lucifier",
                     title='drink water',
                     msg="Drink WATer",
                     duration="short",
                     icon=r'D:\Languages\PYTHON\python programs\Jarvis\Jarvis {Text_Version_1,0}\icon.ico')

toast.set_audio(audio.LoopingCall, loop=False)
toast.show()