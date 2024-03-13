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
    'happy': ('https://open.spotify.com/playlist/2ze9Ez4VNRj5Tf4VvlsgtX?si=HimFzHL9Qg-d2CElsQlxPw&pi=a-dROSCvKfS8C3&nd=1&dlsi=217e653d799044f6',
              '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2ze9Ez4VNRj5Tf4VvlsgtX?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'),
    'sad': ('https://open.spotify.com/playlist/2T7v3TghU7ynz7LhC2G3NH?si=Whi8GJs9Qn-FsJebnLxiIA&pi=a-ue9PFtuARfyt&nd=1&dlsi=cb3a80691f4f4c0d',
            '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2T7v3TghU7ynz7LhC2G3NH?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'),
    'ordinary': ('https://open.spotify.com/playlist/1Vuto5nEee1y2tkFfbr8eZ?si=BPTw66L3RCqlS4tZWZm9Kg&pi=a-WCuZdblkRm-b&nd=1&dlsi=277d820903da4a97',
                 '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/1Vuto5nEee1y2tkFfbr8eZ?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'),
    'upset': ('https://open.spotify.com/playlist/3IAicaLI17kpLAAjvWzZoN?si=ddlr-pB0QMyTH8NG3nNK-Q&pi=a-vFOadQfLQAm4&nd=1&dlsi=fa902665bdd34252',
              '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3IAicaLI17kpLAAjvWzZoN?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>')
    # Add more emotions and playlist URLs as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_playlist', methods=['POST'])
def get_playlist():
    data = request.json
    speech_input = data.get('speech_input', '').lower()

    print(f"Received speech input: {speech_input}")

    # Remove extra characters from the speech input
    cleaned_input = ''.join(c for c in speech_input if c.isalnum() or c.isspace())

    # Extract the emotion from the speech input
    emotion = None
    for word in cleaned_input.split():
        if word in playlist_urls:
            emotion = word
            break

    print("Detected emotion:", emotion)  # Added logging

    if emotion:
        playlist_url = playlist_urls[emotion][0]
        return jsonify({'success': True, 'playlist_url': playlist_url, 'embedCode': playlist_urls[emotion][1]})
    else:
        return jsonify({'success': False, 'message': 'No emotion detected or playlist not found.'})

if __name__ == "__main__":
    app.run(debug=True)
