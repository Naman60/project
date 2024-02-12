import speech_recognition as sr

def speech_to_text():
    # Create a speech recognition object
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Record audio for up to 5 seconds

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Use Google Web Speech API for recognition
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")

if __name__ == "__main__":
    speech_to_text()
