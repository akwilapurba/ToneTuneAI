import logging
import webbrowser
from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG for Flask app

# Configure static file serving
app.static_folder = 'static'  # Specify the folder where static files are located
app.static_url_path = '/static'  # Define the URL prefix for static files

# Define your playlist URLs based on emotions
playlist_urls = {
    'happy': 'https://open.spotify.com/playlist/2ze9Ez4VNRj5Tf4VvlsgtX?si=86a275baa7884b3f&pt=f43baaf6652636a183b89b12018a77aa',
    'sad': 'https://open.spotify.com/playlist/2T7v3TghU7ynz7LhC2G3NH?si=7ed3ac9a2bb449c0&pt=9498f23e44280d045ef18b7020ca3af8',
    'ordinary': 'https://open.spotify.com/playlist/1Vuto5nEee1y2tkFfbr8eZ?si=b687f1e0425b4903&pt=516c656a7386a2ed5320d6b960417878',
    'upset': 'https://open.spotify.com/playlist/3IAicaLI17kpLAAjvWzZoN?si=db8b2a25c26b4d96&pt=6ebe5fd175a356ff6161a57bcfcdb833'
    # Add more emotions and playlist URLs as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_playlist', methods=['POST'])
def search_playlist_route():
    data = request.json
    search_query = data['query']

    # Search for playlist based on user's query
    playlist_url = search_playlist(search_query)
    if playlist_url:
        return jsonify({'success': True, 'playlist_url': playlist_url})
    else:
        return jsonify({'success': False})

@app.route('/get_playlist', methods=['POST'])
def get_playlist():
    data = request.json
    speech_input = data.get('speech_input', '').lower()

    print(f"Received speech input: {speech_input}")

    # Extract the emotion from the speech input
    emotion = None
    for word in speech_input.split():
        if word in playlist_urls:
            emotion = word
            break

    print("Detected emotion:", emotion)  # Added logging

    if emotion:
        playlist_url = playlist_urls[emotion]
        webbrowser.open_new_tab(playlist_url)
        return jsonify({'success': True, 'message': f'Opening {emotion} playlist in a new tab.'})
    else:
        return jsonify({'success': False, 'message': 'No emotion detected or playlist not found.'})

@app.route('/speech_to_playlist', methods=['POST'])
def speech_to_playlist():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio_input = recognizer.listen(source)

    try:
        speech_text = recognizer.recognize_google(audio_input)
        print("Speech recognized:", speech_text)  # Print the recognized speech text
        # Search for playlist based on recognized speech
        playlist_url = search_playlist(speech_text)
        if playlist_url:
            return jsonify({'success': True, 'playlist_url': playlist_url})
        else:
            return jsonify({'success': False, 'message': 'No playlist found for the given speech.'})
    except sr.UnknownValueError:
        return jsonify({'success': False, 'message': 'Speech recognition could not understand audio.'})
    except sr.RequestError as e:
        return jsonify({'success': False, 'message': f'Could not request results from Google Speech Recognition service: {e}.'})

if __name__ == "__main__":
    app.run(debug=True)
