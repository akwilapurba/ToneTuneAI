# emotion_playlist.py
import webbrowser

def play_music_playlist(emotion):
    # Define your playlist URLs based on emotions
    playlist_urls = {
        'happy': 'https://open.spotify.com/playlist/2ze9Ez4VNRj5Tf4VvlsgtX?si=86a275baa7884b3f&pt=f43baaf6652636a183b89b12018a77aa',
        'sad': 'https://open.spotify.com/playlist/2T7v3TghU7ynz7LhC2G3NH?si=7ed3ac9a2bb449c0&pt=9498f23e44280d045ef18b7020ca3af8',
        'neutral': 'https://open.spotify.com/playlist/1Vuto5nEee1y2tkFfbr8eZ?si=b687f1e0425b4903&pt=516c656a7386a2ed5320d6b960417878',
        'angry': 'https://open.spotify.com/playlist/3IAicaLI17kpLAAjvWzZoN?si=db8b2a25c26b4d96&pt=6ebe5fd175a356ff6161a57bcfcdb833'
        # Add more emotions and playlist URLs as needed
    }

    # Play the playlist corresponding to the recognized emotion
    if emotion in playlist_urls:
        webbrowser.open(playlist_urls[emotion])
        print(f"Playing {emotion} playlist...")
    else:
        print("No playlist found for the given emotion.")
