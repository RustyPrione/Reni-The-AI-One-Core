def whatsapp(text):
    from selenium import webdriver
    import pyttsx3
    import speech_recognition as sr
    import time
    if(('send WhatsApp message'==text)|('send a WhatsApp message'==text)):
        r=sr.Recognizer()
        engine=pyttsx3.init()
        sound=engine.getProperty('voices')
        engine.setProperty('voice',sound[1].id)
        engine.say("Whom do you want to send message")
        engine.runAndWait()
        with sr.Microphone()as source:
            print("I'm listening...")
            audio=r.listen(source)
        try:
            name =r.recognize_google(audio)
            print(name)
            driver = webdriver.Firefox()
            driver.get('https://web.whatsapp.com/')
        except Exception as e:
            engine.say("Sorry i couldn't find Firefox webdriver")
            engine.runAndWait()
            engine.say("Please download Gekodriver from github of Mozilla and paste it in my core part")
            engine.runAndWait()
        engine.say("Tell me what message want to send")
        engine.runAndWait()
        with sr.Microphone()as source:
            print("I'm listening...")
            audio=r.listen(source)
        try:
            msg = r.recognize_google(audio)
            print(msg)
        except Exception as e:
            print (e)
        count = 1
        engine.say("Please Scann QR code of from Browser")
        engine.runAndWait()
        time.sleep(10)
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name('_3u328')
        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_3M-N-')
            button.click()
   





















            
