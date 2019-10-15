def androidpwctrl(text):
    import pyttsx3
    import os
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(("shut down my phone"==text)|("shutdown this phone"==text)|("shut down this device"==text)|("shut down my device"==text)):
        engine.say("Okay Shutting down your phone")
        engine.runAndWait()
        os.system("adb.exe shell reboot -p")
        engine.say("Device is Shutdowned and it will be in charging mode")
        engine.runAndWait()
    if(("switch off my device"==text)|("switch off my phone"==text)):
        engine.say("Okay Switching off your Device")
        engine.runAndWait()
        os.system("adb.exe shell reboot -p")
        engine.say("Device is Shutdowned and it will be in charging mode")
        engine.runAndWait()
    if(("switch off this device"==text)|("switch off this phone"==text)):
        engine.say("Okay Switching off this device")
        engine.runAndWait()
        os.system("adb.exe shell reboot -p")
        engine.say("Device is Shutdowned and it will be in charging mode")
        engine.runAndWait()
    if(("power of this device"==text)|("power off this device"==text)):
        engine.say("Okay Turning off that device")
        engine.runAndWait()
        os.system("adb.exe shell reboot -p")
        engine.say("Device is powered off and it will be in charging mode")
        engine.runAndWait()
    if(("power of my device"==text)|("power off my device"==text)):
        engine.say("Okay Turning off your device")
        engine.runAndWait()
        os.system("adb.exe shell reboot -p")
        engine.say("Device is Powered off and it will be in charging mode")
        engine.runAndWait()
    if(("reboot my phone"==text)|("reboot my device"==text)):
        engine.say("Okay Rebooting your device")
        engine.runAndWait()
        os.system("adb.exe shell reboot")
    if(("restart this phone"==text)|("restart this device"==text)):
        engine.say("Okay Restarting phone")
        engine.runAndWait()
        os.system("adb.exe shell reboot")
    if(("restart my device"==text)|("restart my phone"==text)):
        engine.say("Okay Restarting YOUR phone")
        engine.runAndWait()
        os.system("adb.exe shell reboot")
    if(("reboot my device in recovery mode"==text)|("reboot this device in recovery mode"==text)):
        engine.say("Okay Rebooting  device in Recovery Mode")
        engine.runAndWait()
        os.system("adb.exe shell recovery")
    if(("reboot this phone"==text)|("reboot this device"==text)):
        engine.say("Okay Rebooting that device ")
        engine.runAndWait()
        os.system("adb.exe shell reboot")
    if(("reboot this device in bootloader mode"==text)|("reboot this phone in bootloader mode"==text)):
        engine.say("Okay Rebooting  device in bootloader Mode")
        engine.runAndWait()
        os.system("adb.exe shell bootloader")
    if(("reboot my phone in bootloader mode"==text)|("reboot my device in bootloader mode"==text)):
        engine.say("Okay Rebooting your device in Bootloader mode ")
        engine.runAndWait()
        os.system("adb.exe shell bootloader")
