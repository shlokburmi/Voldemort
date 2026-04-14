import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Voldemort")

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source,timeout=2)
        print("recognizing...")
        try:
            command = recognizer.recognize_google(audio)  
            print("You said:", command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error:", e)