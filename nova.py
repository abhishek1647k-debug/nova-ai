import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import os

listener = sr.Recognizer()

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:

        print("Listening...")

        listener.adjust_for_ambient_noise(source, duration=1)

        voice = listener.listen(source, timeout=5)

        command = listener.recognize_google(voice)

        command = command.lower()

        print("You said:", command)

        if "youtube" in command:
            talk("Opening YouTube")
            pywhatkit.playonyt("YouTube")
        
        elif "google" in command:
            talk ("Opening Google")
            webbrowser.open("https://google.com")

        elif "instagram" in command:
            talk ("Opening Instagram")
            webbrowser.open("https://instagram.com")

        elif "spotify" in command:
            talk ("Opening Spotify")    
            webbrowser.open("https://spotify.com")
        
        elif "send message" in command:
            talk ("Sending message")
            pywhatkit.sendwhatmsg_instantly(
                "+919325816033",
                "Hello from Nova AI",
        
            )

        elif "open chrome" in command:
              talk ("Opening Chrome")
              os.startfile("C:\\Program Files\\Google\\chrome\\Application\\chrome.exe")
              
        elif "open calculator" in command:
            talk ("Opening Calculator")
            os.system("calc")
         
        elif "open notepad" in command:
            talk ("Opening Notepad")
            os.system("notepad")
         
        elif "shutdown pc" in command:
            talk("Shutting down your PC")
            os.system("shutdown /s/t/ 5")

        elif "restart pc" in command:
             talk("Restarting your PC")
             os.system("shutdown /r/t/5")

        elif "lock pc" in command:
            talk("Locking your PC")
            os.system("rundll32.exe user32.dll,LockWorkStation")
                     
            import pyautogui
            pyautogui.press ("enter")

        else:
            talk("Command not found")

except Exception as e:
    print("Error:", e)