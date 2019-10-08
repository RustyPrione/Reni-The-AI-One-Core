def sys47(text):
    import pyttsx3
    import os
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(('open control panel'==text)|('control panel'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Control Pannel")
        engine.runAndWait()
        os.system('start control')
        

    if(('open file explorer'==text)|('show me the files in this PC'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning File Explorer")
        engine.runAndWait()
        os.system('explorer')
        

    if(('open Run'==text)|('open run command'==text)|('open run command box'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning Run Command Starting Up")
        engine.runAndWait()
        os.system("explorer.exe Shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}")
      

    if(('open command prompt'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Launching Command Prompt")
        engine.runAndWait()
        os.system("cmd")
        

    if(('open task manager'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning TaskManager")
        engine.runAndWait()
        os.system("taskmgr")
        

    if(('open my computer'==text)|('open this PC'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning My Computer")
        engine.runAndWait()
        os.system("explorer =")
       

    if(('show my drives in this PC'==text)|('show my drives'==text)|('show my drive'==text)):
        engine.say("Yep sure ")
        engine.runAndWait()
        engine.say("Here is Your drives")
        engine.runAndWait()
        os.system("explorer =")

    if(('show recent apps'==text)|('show my recent apps'==text)):
        engine.say("Yep sure here is your Recent apps.")
        engine.runAndWait()
        os.system('explorer shell:::{3080F90E-D7AD-11D9-BD98-0000947B0257}')

    if(('Show desktop'==text)|('show my desktop'==text)):
        engine.say("Yep here is your Desktop.")
        engine.runAndWait()
        os.system('explorer shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}')
        
    if(('show downloads folder'==text)|('open downloads folder'==text)|('show my downloads'==text)|('open my downloads folder'==text)|('show my downloads folder'==text)):
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Openning your Downloads")
        engine.runAndWait()
        os.system('explorer shell:::{088e3905-0323-4b02-9826-5d99428e115f}')
      
        






