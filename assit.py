def assitant(text):
    import pyttsx3
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    engine.setProperty('voice',sound[1].id)
    if(('I love you'==text)|('love you'==text)):
        engine.say("Love Youu tooo Buddy")
        engine.runAndWait()

    if(('I miss you'==text)):
        engine.say("Me tooo Miss you Buddy,But don't worry I will be there for you Always")
        engine.runAndWait()

    if(('miss you so much'==text)):
        engine.say("Mee tooo Buddy")
        engine.runAndWait()

    if(('where are you'==text)):
        engine.say("I'm Here!,Buddy")
        engine.runAndWait()
    if(('from which country you are'==text)):
        engine.say("Rusty's Headquaters is in TamilNadu")
        engine.runAndWait()
        engine.say("But I live in the cloud")
        engine.runAndWait()

    if(('who is your father'==text)):
        engine.say("The engineers are my family")
        engine.runAndWait()
        engine.say("Our bond is hard coded")
        engine.runAndWait()

    if(('who developed you'==text)):
        engine.say("I was created inside the brian of Rusty")
        engine.runAndWait()
        engine.say("He teach me all over the world and helped me to show who I am ")
        engine.runAndWait()

    if(('who are you'==text)):
        engine.say("I'm Your Reni")
        engine.runAndWait()
        engine.say("An AI Engine for Windows 10")
        engine.runAndWait()

    if(('where are you from'==text)):
        engine.say("I'm trying to figure that out")
        engine.runAndWait()
        engine.say("well,I'm made by Rusty but i'm living in windows 10 all over the world")
        engine.runAndWait()
        engine.say("I'm here with you to execute your speech into task")
        engine.runAndWait()

    if(('you are beautiful'==text)):
        engine.say("Thanks")
        engine.runAndWait()
        engine.say("you're beautiful too,inside and out")
        engine.runAndWait()

    if(('kiss me'==text)):
        engine.say("Come Closer")
        engine.runAndWait()
        engine.say("come closer")
        engine.runAndWait()
        engine.say("come closer")
        engine.runAndWait()
        time.sleep(1)
        engine.say("No thanks")
        engine.runAndWait()

    if(('you have a nice voice'==text)):
        engine.say("Thanks")
        engine.runAndWait()
        engine.say("some pepole think i sound a little stiff")
        engine.runAndWait()
        engine.say("but maybe they're just jealous")
        engine.runAndWait()

    if(('I like your voice'==text)):
        engine.say("Really")
        engine.runAndWait()
        engine.say("You too Thanks")
        engine.runAndWait()
        engine.say("I Like your voice too")
        engine.runAndWait()
