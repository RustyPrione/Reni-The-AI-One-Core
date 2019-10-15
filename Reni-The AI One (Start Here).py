import speech_recognition as sr
import os
import pygame
import time
import pyttsx3
import sysdrivers as sysdr
import powerctrl as power
import msapps as app
import system47 as s47
import sysservices as services
import whatsappservices as w
import facebookservices as f
import gmailservices as g
import googleservices as G
import assit as a
import mozilla as m
import pwctrlandroid as p


r=sr.Recognizer()

engine=pyttsx3.init()
sound=engine.getProperty('voices')
engine.setProperty('voice',sound[1].id)
pygame.mixer.init()
pygame.mixer.music.load("start_listen.mp3")
pygame.mixer.music.play()
time.sleep(1)
engine.say("I'm listening")
engine.runAndWait()

with sr.Microphone()as source:
    print("I'm listening...")
    audio=r.listen(source)
    print("Yep sure here you go.")

try:

    text=r.recognize_google(audio)
    sysdr.systemdrivers(text)
    power.powercontrol(text)
    app.apps(text)
    s47.sys47(text)
    services.service(text)
    w.whatsapp(text)
    f.fb(text)
    g.gmail(text)
    G.google(text)
    a.assitant(text)
    m.mozilla(text)
    p.androidpwctrl(text)

    if('hello'==text):
        print("done")
    else:
        print(text)
except Exception as e:
    print (e)
    
