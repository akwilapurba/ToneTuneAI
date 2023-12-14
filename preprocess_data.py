import os
import librosa
import numpy as np

def extract_features(file_path):
    try:
        # Load audio file with a target sampling rate
        audio, sr = librosa.load(file_path, res_type='kaiser_fast', sr=22050)

        # Extract MFCCs (Mel Frequency Cepstral Coefficients)
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

        # Pad or truncate the sequences to a fixed length
        max_len = 40
        if len(mfccs[0]) < max_len:
            pad_width = max_len - len(mfccs[0])
            mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
        else:
            mfccs = mfccs[:, :max_len]

        return mfccs
    except Exception as e:
        print("Error encountered while parsing file: ", file_path)
        return None

def preprocess_data(dataset_path):
    emotions = {'angry': 0, 'disgust': 1, 'fear': 2, 'happy': 3, 'neutral': 4, 'sad': 5, 'surprise': 6}

    X, y = [], []

    for subdir, dirs, files in os.walk(dataset_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            emotion_label = os.path.basename(subdir)

            if emotion_label not in emotions:
                continue

            features = extract_features(file_path)

            if features is not None:
                X.append(features)
                y.append(emotions[emotion_label])

    return np.array(X), np.array(y)

# Usage example:
dataset_path = 'path/to/your/RAVDESS/dataset'
X, y = preprocess_data(dataset_path)