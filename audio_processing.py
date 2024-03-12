import wave
import numpy as np

def capture_audio_from_file(file_path):
    try:
        with wave.open(file_path, 'rb') as wf:
            audio_data = wf.readframes(wf.getnframes())
            # Replace null characters with zeros
            audio_data = audio_data.replace(b'\x00', b'\x00')
            return np.frombuffer(audio_data, dtype=np.int16)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None

def transcribe_audio(audio_data):
    recognizer = sr.Recognizer()

    try:
        recognized_speech = recognizer.recognize_google(audio_data)
        print(f"Recognized speech: {recognized_speech}")
        return recognized_speech
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
