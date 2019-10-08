def mozilla(text):
    import pyttsx3
    import os
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(('open Mozilla'==text)|('open Firefox'==text)|('open Mozilla Firefox'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Launching Firefox")
        engine.runAndWait()
        os.system('start firefox https://www.google.com')
