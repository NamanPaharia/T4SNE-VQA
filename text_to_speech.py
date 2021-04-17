import pyttsx3

def output_audio_from_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
    
