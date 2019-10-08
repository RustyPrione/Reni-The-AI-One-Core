def google(text):
    if(('search in Google'==text)|('search Google'==text)|('search result in Google'==text)):
        import pyttsx3
        import time
        engine=pyttsx3.init() 
        sound=engine.getProperty('voices') 
        engine.setProperty('voice',sound[1].id)
        engine.say("Yep sure What you want to search in Google")
        engine.runAndWait()
        from selenium import webdriver
        import speech_recognition as sr
        r=sr.Recognizer()
        
        with sr.Microphone()as source:
            print("I'm listening...")
            audio=r.listen(source)
            print("Okie...")
        try:
            search=r.recognize_google(audio)
            driver=webdriver.Firefox()
            driver.get("https://www.google.com")
            print(search)
            driver.find_element_by_name("q").send_keys(search)
            time.sleep(3)
            driver.find_element_by_name("btnK").click()
            engine.say("Here My Results In Firefox")
            engine.runAndWait()
        except:
            time.sleep(2)
            driver.find_element_by_name("btnK").click()
            engine.say("Here My Results In Firefox")
            engine.runAndWait()
            print('error')
    
