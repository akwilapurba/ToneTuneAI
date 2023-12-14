# main.py
import speech_recognition as sr
from emotion_playlist import play_music_playlist
from emotion_recognition import recognize_emotion
from data_preparation import preprocess_data
from train_model import build_and_train_model

def capture_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=30)

    return audio

def main():
    # Workflow orchestration
    # dataset_path = 'your_dataset_path.csv'  # Replace with your actual dataset path
    # X_train, X_test, y_train, y_test = preprocess_data(dataset_path)

    # Call preprocess_data without providing a dataset path
    X_train, X_test, y_train, y_test = preprocess_data()

    model = build_and_train_model(X_train, y_train)

    # Capture audio
    audio_data = capture_audio()
    
    # You can pass the trained model to the emotion recognition function
    # Add code for recording audio and recognizing emotion
    emotion = recognize_emotion(model, audio_data)  # Replace audio_data with your actual audio data
    print(f"You feel: {emotion}")

    # Play the corresponding playlist based on the recognized emotion
    play_music_playlist(emotion)

if __name__ == "__main__":
    main()
