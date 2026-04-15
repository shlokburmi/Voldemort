import speech_recognition as sr
import webbrowser
import musicLibrary
import os
from gtts import gTTS
from playsound import playsound

# Initialize recognizer
r = sr.Recognizer()

# 🔊 Speak function (RELIABLE)
def speak(text):
    print("Assistant:", text)

    tts = gTTS(text=text, lang='en', tld='co.in')
    filename = "voice.mp3"

    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# 🎯 Command handler
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

    elif "open x" in command:
        speak("Opening X")
        webbrowser.open("https://www.x.com")

    # 🎵 Play Music
    elif command.startswith("play"):
        song = command.replace("play", "").strip()

        found = False
        for key in musicLibrary.music:
            if song in key:
                speak(f"Playing {key}")
                webbrowser.open(musicLibrary.music[key])
                found = True
                break

        if not found:
            speak("Song not found")
            print("Available songs:", list(musicLibrary.music.keys()))

# 🚀 Main
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

            # 🎤 Wake word
            if "voldemort" in word:
                command = word.replace("voldemort", "").strip()

                if command == "":
                    speak("yeah")   # ✅ ALWAYS speaks now
                else:
                    speak("yeah, tell me")
                    process_command(command)

            else:
                process_command(word)

        except sr.WaitTimeoutError:
            print("No speech detected (timeout)")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

        except Exception as e:
            print("Error:", e)