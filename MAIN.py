from cProfile import label
from cgitb import text
from fnmatch import translate
from re import search
from tkinter import EXCEPTION, font
from bs4 import BeautifulSoup
from click import command
import pyttsx3
from requests_cache import requests
import speech_recognition as sr
import datetime
import webbrowser
import pyautogui
import wikipedia
import os
import keyboard
import playsound
import tkinter as tk
from pytube import YouTube
from googletrans import Translator
from pywikihow import search_wikihow
import cv2





cam=cv2.VideoCapture(0)
count=0

Assistant=pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[1].id)
Assistant.setProperty('rate',175)



def speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f":{audio}")
    print("  ")
    Assistant.runAndWait()

def greet():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak('Good Morning Sir!')
    elif h>=12 and h<18:
        speak('Good afternoon Sir!')
    else:
        speak('Good Evening Sir!')
    speak('I am Crab your virtual assistant. How may I help you sir')

def tc():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Sir..")
        command.pause_threshold=0.5
        audio=command.listen(source)

        try:
            print("Recognizing Sir ......")
            query=command.recognize_google(audio,language='en-in')
            print(f"You said: {query}")
        
        except Exception as error:
            print("Say that again Sir.")
            return None
        return query.lower()


        
def tasks():
    def WhatsApp():
        import pywhatkit
        speak("Please give me the number Sir")
        num='+91'+int(input("Enter number:- "))
        speak("What should I say Sir")
        msg=tc()
        speak("Please Tell me the hour Sir")
        hour=int(tc())
        speak("Please Tell me the minute Sir")
        minute=int(tc())
        pywhatkit.sendwhatmsg(num,msg,hour,minute,20)
        speak("sent Sir")
    def Apps():
        if 'code' in query:
            os.startfile("C:\\Users\\sidha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'epic' in query:
            os.startfile("C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
        elif 'battle' in query:
            os.startfile("F:\Battle.net\\Battle.net Launcher.exe")
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'spotify' in query:
            os.startfile("C:\\Users\\sidha\\AppData\\Roaming\\Spotify\\Spotify.exe")
        elif 'steam' in query:
            os.startfile("C:\\Program Files (x86)\\Steam\\steam.exe")
    def closeApp():
        speak("Ok Sir")
        if 'code' in query:
            os.system("TASKKILL /F / im Code.exe")
        elif 'epic' in query:
            os.system("TASKKILL /F / im EpicGamesLauncher.exe")
        elif 'games' in query:
            os.system("TASKKILL /F / im games")
        elif 'chrome' in query:
            os.system("TASKKILL /F / im chrome.exe")
        elif 'spotify' in query:
            os.system("TASKKILL /F / im Spotify.exe")
        elif 'steam' in query:
            os.system("TASKKILL /F /im steam.exe ")
    def YoutubeAutomation():
        speak("What should I do Sir")
        query=tc()

        if 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'reverse' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif'minimize' in query:
            keyboard.press('i')
    def ChromeAutomation():
        speak("Chrome Automation started Sir")
        comms=tc()
        if 'close this tab' in comms:
            keyboard.press_and_release('ctrl+w')
        elif 'open new tab' in comms:
            keyboard.press_and_release('ctrl+t')
        elif 'open new window' in comms:
            keyboard.press_and_release('ctrl+n')
        elif 'history' in command:
            keyboard.press_and_release('ctrl+h')
    def dict():
        from PyDictionary import PyDictionary as dictionary
        speak("What should I search Sir")
        comm=tc()
        if 'meaning' in comm:
            comm=comm.replace("what is the","")
            comm=comm.replace("meaning","")
            comm=comm.replace("of ","")
            comm=comm.replace(" ","")
            result=dictionary.meaning(comm)
            speak(f"The meaning of {comm} is {result}")
        elif 'synonym' in comm:
            comm=comm.replace("what is the","")
            comm=comm.replace("synonym","")
            comm=comm.replace("of ","")
            comm=comm.replace(" ","")
            result=dictionary.synonym(comm)
            speak(f"The synonym of{comm} is {result}")
        elif'antonym' in comm:
            comm=comm.replace("what is the antonym ","")
            comm=comm.replace("of ","")
            comm=comm.replace("antonym","")
            comm=comm.replace(" ","")
            result=dictionary.antonym(comm)
            speak(f"The antonym of {comm} is {result}")
    def ss():
        speak("Ok Sir, What should I name the File?")
        path=tc()
        pathname=path +".png"
        path1="F:\\ScreenShot\\"+pathname
        sh=pyautogui.screenshot()
        sh.save(path1)
        os.startfile("F:\\ScreenShot")
        speak("Done Sir")

    def th():
        command=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening Sir..")
            command.pause_threshold=1
            audio=command.listen(source)

            try:
                print("Recognizing Sir ......")
                query=command.recognize_google(audio,language='hi')
                print(f"You said: {query}")
            
            except Exception as error:
                print("Say that again Sir.")
                return None
            
            return query
    
    def Trans():
        speak("What should I translate Sir.")
        line = th()
        tlt=Translator()
        result=tlt.translate(line,dest='en')
        text=result.text
        speak("The translation is "+text)

    
    def Temp():
        search = "temperature in hissar"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature}.")

        speak("Do you wantt me to tell the temprature of another place Sir ?")
        next = tc()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = tc()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            speak("no problem sir")


    greet()
    while True :
        query=tc()
        try:
            if 'hello' in query:
                speak("Hello Sir")
            elif 'how are you' in query:
                speak("I am Fine Sir.")
                speak("How about you.")
            elif 'you need a break' in query:
                speak("Okay Sir, Hope to see you soon . Call me any time sir.")
                break
            
            
            elif 'bye' in query:
                speak("Good Bye Sir.")
                break
            
            elif 'change voice' in query:
                Assistant.setProperty('voices',voices[0].id)
            
            
            elif 'original voice' in query:
                Assistant.setProperty('voices',voices[1].id)
            
            
            
            elif 'search youtube' in query:
                speak("Ok Sir , This is what I found Sir")
                query=query.replace("search youtube for","")
                web='https://www.youtube.com/results?search_query='+query
                webbrowser.open(web)
                speak("Done Sir")
            
            
            
            elif 'search google' in query:
                import wikipedia as googleScrap
                import pywhatkit
                query=query.replace("search google","")
                query=query.replace("google","")
                speak("This is what I found on the web.")
                try:
                    pywhatkit.search(query)
                    result=googleScrap.summary(query,3)
                    speak(result)               
                except:
                    speak("No speakable data found Sir.")         
            
            
            
            elif 'launch website' in query:
                speak("Sir please tell me the name.")
                query=tc()
                query=query.replace(" ","")
                speak("Ok Sir, Launching ")
                web='https://www.'+query+'.com'
                webbrowser.open(web)
                speak("Done Sir")
            
            
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/")
            
            
            
            
            elif 'play' in query:
                import pywhatkit
                query=query.replace('play','')
                speak('playing'+query)
                pywhatkit.playonyt(query) 

            
            
            
            elif 'wikipedia' in query:
                speak('Searching wikipedia Sir...')
                query=query.replace('wikipedia','')
                results=wikipedia.summary(query,sentences=3)
                speak('According to wikipedia')
                print(results)
                speak(results)
            
            
            
            elif 'whatsapp message' in query:
                WhatsApp()
            
            
            
            elif 'screenshot' in query:
                ss()
            
            
            
            elif 'launch' in query:
                speak("OK Sir")
                Apps()
            
            elif 'close' in query:
                speak("OK sir")
                closeApp()
            
            
            elif"automate youtube" in query:
                YoutubeAutomation()
            
            
            elif 'pause' in query:
                keyboard.press('space bar')
            
            
            elif 'restart' in query:
                keyboard.press('0')
            
            
            elif 'mute' in query:
                keyboard.press('m')
            
            
            elif 'skip' in query:
                keyboard.press('l')
            
            
            elif 'reverse' in query:
                keyboard.press('j')
            
            
            
            
            elif 'full screen' in query:
                keyboard.press('f')
            
            
            
            elif'minimize' in query:
                keyboard.press('i')
            
            
            elif'automate chrome' in query:
                ChromeAutomation()
            
            
            elif 'close this tab' in query:
                keyboard.press_and_release('ctrl+w')
            
            
            
            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl+t')
            
            
            elif 'open new window' in query:
                keyboard.press_and_release('ctrl+n')
            
            
            
            elif 'history' in query:
                keyboard.press_and_release('ctrl+h')
            
            
            elif 'joke' in query:
                import pyjokes
                get=pyjokes.get_joke()
                speak(get)
            
            
            elif"repeat my words" in query:
                speak("speak sir")
                comm=tc()
                speak(f"You said: {comm}")
            
            
            elif'my location' in query:
                speak("Ok Sir, Wait a minute")
                webbrowser.open("https://www.google.com/maps/@30.5160911,76.6575891,17z")
            
            
            elif 'dictionary' in query:
                dict()
            

            elif'alarm' in query:    
                speak("What Time should I set sir")
                time=input("ENTER TIME")
                
                while True:
                    
                    Time_Ac=datetime.datetime.now()
                    now=Time_Ac.strftime("%H:%M:%S")
                    
                    
                    if now==time:
                        speak("Time to wake up Sir")
                        playsound('Auratone.mp3')
                        speak("I am stoping the alarm Sir")
                    
                    
                    elif now>time:
                        break
            elif 'video downloader' in query:
                root=tk.Tk()
                canvas1=tk.Canvas(root,width=400,height=300,relief='raised',bg='black')
                canvas1.pack()

                label1=tk.Label(root,text='YouTube Video Downloader')
                label1.config(font=('helvetica',14))
                canvas1.create_window(200,25,window=label1)


                label2=tk.Label(root,text="Enter Video Url")
                label1.config(font=('helvetica',10))
                canvas1.create_window(200,100,window=label2)

                entry1=tk.Entry()
                canvas1.create_window(200,140,window=entry1)

                def download():
                    ytd_url=entry1.get()
                    try:
                        obj=YouTube(ytd_url)
                        filter=obj.streams.filter(progressive=True,file_extension='mp4')
                        speak("Please enter the name sir")
                        name=input()+'.mp4'
                        filter.get_highest_resolution().download(filename=name)
                        label3=tk.Label(root,text="Downloading...",font=('helvetica',10))
                        canvas1.create_window(200,210,window=label3)
                    except EXCEPTION as e:
                        label4=tk.label(root,text='Download failed',font=('helvetica',10))
                        canvas1.create_window(200,210,window=label4)
                button1=tk.Button(text='Download',command=download,bg='black',fg='red',font=('helvetica',9,'bold'))
                canvas1.create_window(200,180,window=button1)

                root.mainloop()

                
            elif "picture" in query:
                while True:
                    ret, frame =cam.read()
                    cv2.imshow('CRAB', frame)
                    if cv2.waitKey(10)==ord('e'):
                        break
                cam.release()
                cv2.destroyAllWindows()

            
            elif 'translate' in query:
                Trans()
            
            elif 'temperature' in query:
                Temp()
            
            elif 'how to' in query:
                speak("Getting data from the internet")
                max_result=1
                fxn=search_wikihow(query,max_result)
                assert len(fxn)==1
                fxn[0].print()
                speak(fxn[0].summary)
            
            elif None in query:
                print("Sorry I didn't understand that Sir")
        except Exception as e:
            print(e)
            print("Say that again Sir")