def fb(text):
    if(('open Facebook'==text)):
        import pyttsx3
        import os
        engine=pyttsx3.init()
        sound=engine.getProperty('voices')
        engine.setProperty('voice',sound[1].id)
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        engine.say("Opening FaceBook In Firefox")
        engine.runAndWait()
        os.system('start firefox https://www.facebook.com')
    if(('open my Facebook'==text)|('show my Facebook'==text)):
        import pyttsx3
        import x as xx
        engine=pyttsx3.init()
        sound=engine.getProperty('voices')
        engine.setProperty('voice',sound[1].id)
        engine.say("Yep sure here you go.")
        engine.runAndWait()
        from selenium import webdriver
        driver=webdriver.Firefox()
        driver.get("https://www.facebook.com/login/")
        engine.say("Opening FaceBook and Logging In your Account")
        engine.runAndWait()
        e=xx.e()
        p=xx.p()
        try:
            email=driver.find_element_by_id("email")
            email.send_keys(e)
            password=driver.find_element_by_id("pass")
            password.send_keys(p)
            login=driver.find_element_by_id("loginbutton")
            login.click()
            engine.say("Enjoy By Reading your News Feed")
            engine.runAndWait()
        except:
            print(e)
    
   
        
            

   
    

