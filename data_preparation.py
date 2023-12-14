# data_preparation.py
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder

def preprocess_data():
    # Example: Define your predefined playlist data
    playlist_data = [('happy', 1), ('sad', 2), ('neutral', 3), ('angry', 4)]

    # Example: Extract features from playlist_data
    X = np.array([extract_features(row) for row in playlist_data])

    # Example: Encode emotion labels
    le = LabelEncoder()
    y = le.fit_transform([emotion for emotion, _ in playlist_data])
    y = to_categorical(y, num_classes=len(le.classes_))

    # Example: Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def extract_features(row):
    # Implement your logic to extract features from the data
    # This might involve processing 'other_feature' or other features
    _, other_feature = row
    # ...

    return other_feature
