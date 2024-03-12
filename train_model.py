from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def build_and_train_model(x_train, y_train):
    input_shape = x_train.shape[1]  # Assuming the shape of your training data is (num_samples, num_features)
    num_classes = y_train.shape[1]   # Assuming one-hot encoding for the labels

    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_shape,)),
        Dense(32, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    # Save the model in the native Keras format
    model.save('emotion_model.keras')

    return model
