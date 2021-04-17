import speech_recognition as sr      
    
def get_text_from_speech(wav_file_path=None):
    r = sr.Recognizer()

    if not wav_file_path:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    
    else:
        with sr.WavFile(wav_file_path) as source:             
            audio = r.record(source)

    try:
        return r.recognize_google(audio)
    except Exception as e:
        print("Error :  " + str(e))
        return None