import speech_recognition as sr
import wave
import numpy as np
from audio_processing import capture_audio_from_file, transcribe_audio
from playlist_search import search_playlist
from data_preparation import preprocess_data
from train_model import build_and_train_model

def main():
    # Workflow orchestration
    dataset_path = 'dataset.csv'

    # Preprocess data
    x_train, x_test, y_train, y_test = preprocess_data(dataset_path)

    model = build_and_train_model(x_train, y_train)

    # Capture audio from file
    audio_file_path = 'D:\PRESUNIV_FILE\Semester5\Artificial_Intelligence\GroupProjectToneTune\ToneTune\audio\0.wav'  # Replace with the actual path to your audio file
    audio_data = capture_audio_from_file(audio_file_path)

    if audio_data is not None:
        # Recognize emotion from audio data
        emotion = recognize_emotion(model, audio_data)
        print(f"You feel: {emotion}")

        # Send the recognized emotion to the Flask server
        url = 'http://localhost:5000/get_playlist'
        payload = {'emotion': emotion}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                playlist_url = response.json().get('playlist_url')
                if playlist_url:
                    print(f"Opening playlist for: {emotion}")
                else:
                    print("No playlist found for the recognized emotion.")
            else:
                print("Error:", response.text)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
