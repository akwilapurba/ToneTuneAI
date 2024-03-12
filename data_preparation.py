# data_preparation.py
import numpy as np
import librosa
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder

def preprocess_data(dataset_path):
    # Load your dataset from the provided path or use any other logic to load your data
    # Example: Load CSV data
    playlist_data = np.genfromtxt(dataset_path, delimiter=';', encoding='utf-8', skip_header=1, dtype=None)

    print("Playlist Data:")
    print(playlist_data)

    # Extract features from playlist_data
    X = np.array([extract_features(audio_data) for emotion, audio_data in playlist_data])

    # Encode emotion labels
    le = LabelEncoder()
    y = le.fit_transform([emotion.encode('utf-8') for emotion, _ in playlist_data])
    y = to_categorical(y, num_classes=len(le.classes_))

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def extract_features(audio_data, sampling_rate=22050, n_mfcc=13):

    audio_data = audio_data.astype(float)
    # flatten
    audio_data = audio_data.flatten()

    # Extract MFCC features from audio_data
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sampling_rate, n_mfcc=n_mfcc)
    mean_mfccs = np.mean(mfccs.T, axis=0)

    return mean_mfccs
