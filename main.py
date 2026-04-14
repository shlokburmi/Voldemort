import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    print("Command:", command)

if __name__ == "__main__":
    speak("Initializing Voldemort")

    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "voldemort":
                speak("Yes, I am here. How can I assist you?")

                with sr.Microphone() as source:
                    print("Voldemort Active...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)

                command = r.recognize_google(audio)
                process_command(command)

        except sr.WaitTimeoutError:
            print("No speech detected (timeout)")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error:", e)