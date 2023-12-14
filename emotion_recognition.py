# emotion_recognition.py
import numpy as np
from data_preparation import extract_features  # Import the extract_features function from data_preparation

def recognize_emotion(model, audio_data):
    # Use the trained model to recognize emotion from audio data
    features = extract_features(audio_data)  # Use the extract_features function from data_preparation
    features = np.array(features).reshape(1, -1)
    predictions = model.predict(features)

    # Get the predicted emotion label
    emotion_label = get_emotion_label(predictions)
    return emotion_label

def get_emotion_label(predictions):
    # Assuming your model has 4 output classes corresponding to emotions (adjust as needed)
    emotion_classes = ['happy', 'sad', 'neutral', 'angry']
    predicted_class = np.argmax(predictions)
    return emotion_classes[predicted_class]
