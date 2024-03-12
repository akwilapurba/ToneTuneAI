import logging
from flask import Flask, render_template, request, jsonify
from playlist_search import search_playlist
from emotion_playlist import playlist_urls
import speech_recognition as sr

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG for Flask app

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
    emotion = data.get('emotion', '').lower()

    if emotion in playlist_urls:
        return jsonify({'success': True, 'playlist_url': playlist_urls[emotion]})
    else:
        return jsonify({'success': False, 'message': 'No playlist found for the given emotion.'})

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
