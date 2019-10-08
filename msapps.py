def apps(text):
    import pyttsx3
    import os
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(('open Paint'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("starting up...")
        engine.runAndWait()
        os.system('mspaint')
        
    if(('open Notepad'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("starting up...")
        engine.runAndWait()
        os.system('notepad')
        
    if(('open camera'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("starting up...")
        engine.runAndWait()
        os.system('start microsoft.windows.camera:')
        
    if(('open settings'==text)|('open Windows settings'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Windows Settings")
        engine.runAndWait()
        os.system('start ms-settings:')
        
    if(('show me the calendar'==text)|('open calendar'==text)|('show calendar'==text)|('show me this month in calendar'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Calander")
        engine.runAndWait()
        os.system('start outlookcal:')
    
    if(('open music player'==text)|('play music'==text)):      
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Launching Groove Music")
        engine.runAndWait()
        os.system("start mswindowsmusic:")
        
    if(('open calculator'==text)|('open Kalsi'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("starting up...")
        engine.runAndWait()
        os.system('calc')

    if(('open alarm'==text)|('set alarm'==text)|('open Stopwatch'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Alaram & Clock")
        engine.runAndWait()
        os.system('explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App')

    if(('open Internet Explorer'==text)|('open Microsoft edge'==text)|('open explorer'==text)|('open edge'==text)|('open Edge'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        if(('open Internet Explorer'==text)|('open explorer'==text)):
           engine.say("Openning Internet Explorer")
           engine.runAndWait()
           os.system('start iexplore')
           wb.get(browser_path).open('www.google.com')
        if(('open Microsoft edge'==text)|('open edge'==text)|('open Edge'==text)):
           engine.say("Openning Microsoft edge")
           engine.runAndWait()
           os.system('start microsoft-edge:https://www.google.com')

    if(('open photos'==text)|('open my gallery'==text)|('show my gallery'==text)|('open my photos'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        if(('open photos'==text)|('open my photos'==text)):
            engine.say("Openning Photos")
            engine.runAndWait()
            os.system('start ms-photos:')
        if(('open my gallery'==text)|('show my gallery'==text)):
            engine.say("Openning Gallery")
            engine.runAndWait()
            os.system('start ms-photos:')

    if(('open Windows security'==text)|('open Windows security settings'==text)|('open Windows Defender'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Windows Security")
        engine.runAndWait()
        os.system('start windowsdefender:')
        print('starting up...')

    if(('open video player'==text)|('open movies and TV'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Video Player")
        engine.runAndWait()
        os.system('start mswindowsvideo:')
        print('starting up...')

          
           
           

    

