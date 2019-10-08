def service(text):
    import pyttsx3
    import os
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(('disconnect Wi-Fi'==text)):
        engine.say("Yep sure")
        engine.runAndWait()
        engine.say("Disconnecting from connected WiFi Network")
        engine.runAndWait()
        os.system("netsh wlan disconnect")
        print('starting up...')

    if(('show Wi-Fi'==text)|('show Wi-Fi network'==text)|('show me Wi-Fi network'==text)|('show available Wi-Fi network'==text)|('show me available Wi-Fi network'==text)|('open Wi-Fi network'==text)):
        engine.say("Yep sure")
        engine.runAndWait()
        os.system("start ms-availablenetworks:")
        print('starting up...')

    if(('show notifications'==text)|('show notification'==text)|('show notification panel'==text)|('show my notifications'==text)|('show my notification'==text)):
        engine.say("Yep sure")
        engine.runAndWait()
        engine.say("Here is your Notification Pannel")
        engine.runAndWait()
        os.system("start ms-actioncenter:")
        print('starting up...')
