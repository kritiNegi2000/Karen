import datetime
import karen
import webbrowser
import random
import pyautogui
import os
import wikipedia

def wishme():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        karen.speak("Good morning sir")
    elif time>=12 and time<18:
        karen.speak("Good afternoon sir") 
    else:
        karen.speak("Good evening sir")

def stop():
    reply=["Have a great day sir",
           "Have a nice day sir",][random.randrange(2)]
    return reply
    
def open_google():
    karen.speak("Opening google")
    webbrowser.open('google.com')

def close():
    pyautogui.moveTo(1900,0)
    pyautogui.click()

def open_youtube():
    karen.speak("Opening youtube")
    webbrowser.open('youtube.com')

def open_10fastfingers():
    karen.speak("Opening 10 fast fingers")
    webbrowser.open("https://10fastfingers.com/typing-test/english")

def open_wordpad():
    path="c:\\Program Files\\Windows NT\\Accessories\\wordpad"
    karen.speak("Opening wordpad")
    os.startfile(path)

def open_code():
    path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    karen.speak("Opening visual studio code")
    os.startfile(path)

def rand():
    options=[1,2,3,4,5,6,0][random.randrange(7)]
    return options

def music():
    path="c:\\Users\\DELL\\Desktop\\Music"
    songs=os.listdir(path)
    select=rand()
    print(songs)
    karen.speak("Playing music")
    os.startfile(os.path.join(path,songs[select]))

def day():
    day=int(datetime.datetime.isoweekday(datetime.datetime.now()))
    if day==1:
        karen.speak("Sir today is monday")
    elif day==2:
        karen.speak("Sir today is tuesday")
    elif day==3:
        karen.speak("Sir today is wednesday")
    elif day==4:
        karen.speak("Sir today is thursday")
    elif day==5:
        karen.speak("Sir today is friday")
    elif day==6:
        karen.speak("Sir today is saturday")
    else:
        karen.speak("Sir today is sunday")

def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    karen.speak(f"Sir the time is {time}")

def date():
    date=int(datetime.datetime.now().day)
    karen.speak(f"Sir today is {date}")

def google_it(query):
    pyautogui.moveTo(900,80)
    
    pyautogui.hotkey('ctrl','t')
    pyautogui.click()
    pyautogui.typewrite(query)
    pyautogui.press('enter')

def Wikipedia(parameter):
    karen.speak("Searching")
    result=wikipedia.summary(parameter,sentences=2)
    karen.speak(result)

