def powercontrol(text):
    import pyttsx3
    import os
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(('shutdown my PC'==text)):
        engine.say("Okay Shutting down your PC")
        engine.runAndWait()
        engine.say("See you soon buddy")
        engine.runAndWait()
        os.system('shutdown /p')
       
    if(('restart my PC'==text)):
        engine.say("Okay Restarting your PC")
        engine.runAndWait()
        engine.say("I will be back in one minute buddy")
        engine.runAndWait()
        os.system('shutdown /r')
        
    if(('go to sleep mode'==text)|('go to sleep'==text)):
        engine.say("Okay I'm Gonna Sleep")
        engine.runAndWait()
        engine.say("Once you come wake up me buddy")
        engine.runAndWait()
        os.system(' RUNDLL32.EXE powrprof.dll,SetSuspendState 0,1,0')
        
    if(('log of this user'==text)):
        engine.say("Okay Signing out from this user")
        engine.runAndWait()
        os.system('shutdown /l')
        
     
