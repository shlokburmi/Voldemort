import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()
    print("Processing:", command)

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open x" in command or "open x" in command:
        speak("Opening x")
        webbrowser.open("https://www.x.com")

    else:
        speak("Sorry, I didn't understand that command")

if __name__ == "__main__":
    speak("Initializing Voldemort")

    while True:
        print("\nListening for command...")

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=4)

            word = r.recognize_google(audio)
            print("Heard:", word)

            word = word.lower()

            # Handle wake word (optional)
            if "voldemort" in word:
                speak("Yes, I am here")
                command = word.replace("voldemort", "").strip()
            else:
                command = word

            if command:
                process_command(command)

        except sr.WaitTimeoutError:
            print("No speech detected (timeout)")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except Exception as e:
            print("Error:", e)