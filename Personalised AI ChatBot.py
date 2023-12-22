import datetime, webbrowser, os, time
from winotify import Notification, audio

import wikipedia as wiki

from subprocess import call
import ctypes

import requests
import random
import AppOpener

def ask():
    user_query = str(input("User: "))
    return user_query

def arguements():
    say(random.choice('yes', "no"))
def say(str):
    print(f'Bot:  {str}')
def say_end(str,end_with='\n'):
    print(f'Bot:  {str}',end=end_with)

def sites(site):
    website_link = {'instagram': "instagram.com",
                       'chat gpt': 'chat.openai.com',
                       'youtube music': 'music.youtube.com',
                       'youtube': 'youtube.com',
                       'google': 'google.com',
                       'github': 'github.com',
                       'gmail': 'https://mail.google.com/'}

    # say("in")
    say(f"Opening {site}")
    link=website_link.values()
    link=list(link)
    names=website_link.keys()
    names=list(names)
    try:
        link_to=link[names.index(site)]
        webbrowser.open(f'{link_to}')
        print(site)
        say(f"Opened {site}")
    except ValueError:
        webbrowser.open(f'{site}.com')

# def OpenDir
def OpenApp(app_name):
    say(f"Opening {app_name.removeprefix('open')}")
    AppOpener.open(app_name,output=False,match_closest=True)
    say(f"Opened {app_name.removeprefix('open')}!")
def drink_Water():
    call(["python", "water_notification.py"])

def CloseApp(App_name):
    say(f"Closing {App_name}")
    AppOpener.close(App_name,output=False,match_closest=True)
    say(f"Closed {App_name}")
def wishMe():
    call(["python", "WishMe.py"])

def wiki_search(user_query):
    cmd_title ,cmd_query =user_query.replace("search","").replace("wikipedia",'').replace("in"or"about"or"for","").strip(),cmd_title.removesuffix("about")
    search_results = wiki.summary(cmd_query)
    say("Here\'s your results")
    say("*results may not be accurate*")
    ctypes.windll.user32.MessageBoxW(0, search_results, f'''Searches {cmd_title}''', 0)
    say("You may continue:)")

def get_weather(user_query):
    say("Opening your request, Hang on tight!",)
    user_query = user_query.replace("get", "").capitalize()
    webbrowser.open(f"{user_query}")
    say("Opened the weather forcast  for your requested city!")

def Clear_Cache():
    try:
        path1 = r"C:\Windows\Temp"
        path2=r'C:\Users\sahil\AppData\Local\Temp'
        for file in os.listdir(path1):
            os.remove(file)
        for file in os.listdir(path2):
            os.remove(file)
        say("Cleared your memory(cache)")
    except WindowsError as e:
        return e

try:
    wishMe()
    while True:
        user_query = ask()
        if 'open' in user_query:

            #opening websites
            if 'website' in user_query or 'site' in user_query :

                user_query=user_query.replace("open website",'')
                sites(user_query)

            # Opening apps commands proceeds
            elif "app" in user_query:
             OpenApp(user_query.replace("open ",'').replace("app ",''))
            # Opening DIRS
            elif 'directory' in user_query or 'dir' in user_query :


                say(f'''Opening {user_query.removeprefix("open").replace("directory",'').strip()} ''')
                os.startfile(f'''C:\\Users\\sahil\\{user_query.removeprefix("open").replace("directory"or"dir",'').strip()}''')
                say(f'''Opened {user_query.removeprefix("open").replace("directory"or"dir",'').strip()} Dir''')

            else:
                say("What do you wanna open?")
                for i in list(["directory",'app','website']):
                    if i!=user_query:
                        say_end(f"{i}?")
                say("just write `open {dir/app/website} {name}`")

             # play dirext video /song from youtube
        elif 'play ' in user_query:
            query=user_query.replace("play",'').capitalize()
            say(f"Playing `{query}` in youtube")
            webbrowser.open(f"https://youtube.com/results?search_query={query}")
        elif 'time' in user_query:
            if ("whats"and'the') in user_query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"{strTime}")
            elif '?' in user_query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"if you asked about `what\'s the time` \n then it\'s {strTime}")
        elif 'search' in user_query:
            if 'module' in user_query:
                user_query = user_query.replace("search module ", "").capitalize()
                say("Opening `docs.python` , `pypi.org` and `python.org` for you:)")
                search_Query1 = webbrowser.open(f"pypi {user_query}")
                search_Query2 = webbrowser.open(f"docs.python. org {user_query}")
                search_Query3=webbrowser.open(f'python.org {user_query}')
                say("Opened!\n    now go and continue your search!")
            elif "wikipedia" in user_query:
                wiki_search(user_query)

        elif 'browse' in user_query:
            query=user_query.replace("browse ",'').capitalize()
            say(f"doing your research about `{query}`")
            say("Opening browser for the results!")
            time.sleep(1)
            webbrowser.open(query)
            say("Opened browser")
        elif 'minimize' in user_query:

            os.startfile(r"C:\Users\Default\AppData\Local\Microsoft\Windows\WinX\Group1\1 - Desktop.lnk")
        elif 'show desktop' in user_query or 'show desktop'.capitalize() in user_query or 'minimize to taskbar' in user_query:
            os.startfile(r"C:\Users\Default\AppData\Local\Microsoft\Windows\WinX\Group1\1 - Desktop.lnk")

        elif'clear' in user_query and 'cache' in user_query:
            Clear_Cache()



        # elif 'set' in user_query:
        # if 'reminder' in user_query:
        # if 'water'  in user_query:

        #     say("Do you wanna turn on your \`drink water reminder\`?\n**it can be turn off**")
        #     drink_water_on = ask()
        #     if drink_water_on == "yes" or drink_water_on == 'on':
        #         say("Your `drink water notifier` is on")
        #         drink_Water()
        #
        #     elif drink_water_on != (('yes' or 'on') or ('no' or 'off')):
        #         say("i didn\'t understand that!")
        #     else:
        #         say("i can\'t turn it off!")
        #         say("Sorry!")
        elif 'get' in user_query:
            if 'weather' in user_query:
                if user_query.replace((("get weather"or "get weather forecast")and "for"),"") =="":
                    say("getting Forecast based on your location.since, you didn\'t provide an input for location")
                    get_weather(user_query)
                    say("Opened Weather Forecast based on your location:)")
                else:
                    user_query.replace((("get weather"or "get weather forecast")and "for"),"").capitalize()
                    get_weather(user_query)
            elif ('bot'and'info') in user_query:
                say("Here are my information:\n     Name : Lucifier   ;\n     Birth: 01/07/2023 ;\n     Made by: Sahil:)  ;")
            elif ('all' and 'functions') in user_query:
                say("i can do all this things:\n     ~getting weather info and time;\n     ~Can do searches for you;\n    ~Can open specific sites-\n       {`instagram`\n       ,`youtube`,`ChatGPT`\n       ,`YT Music`,`Spotify`};\n     ~can open apps - \n       {Vscode,spotify,python\n       ,paint,notepad, edge,\n        terminal, brave, notion,\n       discord, github desktop,\n       cmd,file explorer, telegram,\n        opera gx browser, control panel};\n     ~ Can remind you to drink water;")

        # engaging in casual converstional
        elif 'hi'  in user_query or 'Hi'  in user_query or 'Hey' in user_query or 'Hello' in user_query or 'hey' in user_query or 'hello' in user_query:

            greets = ['Hi, nice to meet you!', 'oh hi:)', 'Hi master , what are you upto now?',
                          ]
            say(random.choice(greets))

        elif 'okay'in user_query or 'ok'in user_query or'OK'in user_query or'Ok'in user_query or'oky'in user_query or'Okyy'in user_query :
            responses=['Yeah','Yup','Yes','Nvm:)','Always on your service!']
            say(random.choice(responses))


        elif 'Bye' in user_query or 'bye' in user_query or "take rest" in user_query:
            exiting_code= ["Thank you for using me........!",'Thank you for making me a part of your screen time \n     now you go and take rest, bye!','i appreciate your interest in me!\n     For now im going off as you asked \n    Thank you master']
            say(random.choice(exiting_code))
            exit()
        elif 'how are you' in user_query:
            replies=["I\'m absolutely fine, wby?","I\'m doing great.\n what about you?", "i\'m great,you?"]
            say(random.choice(replies))
        elif 'im great' in user_query or 'im good' in user_query or 'i doing great' in user_query or 'im fine' in user_query or 'im fine too' in user_query:
            replies=["Great king!👑",'Good to hear that','Nice...','Keep moving on then  brotherrr!!📈','feels good to hear that you are okay']
            say(random.choice(replies))
        elif 'yep' in user_query or'yes' in user_query or'yup' in user_query or'yeah' in user_query:
            responses=['great!👍',"OG😶‍🌫️",'okay!','Ok','ok']
            say(random.choice(responses))
        elif 'close' in user_query:
            user_query= user_query.replace("close ",'')
            CloseApp(user_query)

        else:
            say("Sorry, i didn\'t understand that please repeat:)")
except Exception as e:
    print(e)
# say("You can continue!")
# e=Exception
# with open(r"errors.txt","w+") as file:
#     file.write(e)
#     file.close()

finally:
    exit()
    # print("\n")
    # say('Sorry for the issue i ran in to a problem \n'
    #     "     if you want to exit type `exit` or press `stop`\n"
    #     "     If you want to give FeedBack type`feedback`\n"
    #     )
    # show_not = ask()
    # if show_not == 'exit':
    #     say("Thank you for using me!")
    #     exit()
    # elif show_not == 'feedback':
    #     say("you can give your feedback now:)")
    #     give_feedback = ask()
    #     if give_feedback != '' or give_feedback == '':
    #         say("Thank you for giving your feedback")
    #

