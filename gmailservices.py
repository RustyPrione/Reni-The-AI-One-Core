def gmail(text):
    if(('open my Gmail'==text)|('show my Gmail'==text)):
        from selenium import webdriver
        import time
        import x
        import pyttsx3
        engine=pyttsx3.init()
        sound=engine.getProperty('voices')
        engine.setProperty('voice',sound[1].id)
        engine.say("Yep sure here you go")
        engine.runAndWait()
        driver=webdriver.Firefox()
        driver.get('http://www.gmail.com')
        engine.say("Opening Gmail and Logging In your Account")
        engine.runAndWait()
        driver.find_element_by_name("identifier").send_keys(x.p())
        driver.find_element_by_class_name("RveJvd").click()
        time.sleep(5)
        driver.find_element_by_name("password").send_keys(x.p())
        driver.find_element_by_class_name("RveJvd").click()
        engine.say("Here is Your Mail Box")
        engine.runAndWait()
    if(('open Gmail'==text)):
        import pyttsx3
        import os
        engine=pyttsx3.init()
        sound=engine.getProperty('voices')
        engine.setProperty('voice',sound[1].id)
        engine.say("yep sure Opening Gmail in Firefox")
        engine.runAndWait()
        os.system('start firefox http://www.gmail.com')
        



