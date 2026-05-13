import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser

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

        else:
            talk("Command not found")

except Exception as e:
    print("Error:", e)