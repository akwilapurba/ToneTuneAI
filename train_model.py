# train_model.py
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical  # Add this import
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def build_and_train_model(X, y):
    # Build your deep learning model (modify this based on your needs)
    model = Sequential()
    model.add(Dense(128, input_shape=(X.shape[1],), activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(len(np.unique(y)), activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Convert emotion labels to one-hot encoding
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    y_encoded = to_categorical(y_encoded, num_classes=len(le.classes_))

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    # Save the trained model
    model.save('emotion_model.h5')

    return model
