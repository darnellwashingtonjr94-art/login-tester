import speech_recognition as sr

def verify_voice_command(expected_phrase="execute"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for voice verification phrase...")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio).lower()
            print(f"Heard: {text}")
            if expected_phrase in text:
                print("Voice verification passed.")
                return True
        except Exception as e:
            print(f"Voice recognition error: {e}")
            
    print("Voice verification failed.")
    return False
