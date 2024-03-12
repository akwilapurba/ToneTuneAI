document.getElementById('startRecording').onclick = function() {
    var recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    
    recognition.onstart = function() {
        console.log('Speech recognition started...');
    };
    
    recognition.onresult = function(event) {
        var speechResult = event.results[0][0].transcript;
        console.log('Speech recognized:', speechResult);
        sendSpeechToServer(speechResult);
    };
    
    recognition.onerror = function(event) {
        console.error('Speech recognition error:', event.error);
    };
    
    recognition.onend = function() {
        console.log('Speech recognition ended.');
        // After speech recognition ends, send a request to get the playlist
        fetchPlaylist(emotion); // Pass the emotion variable here
    };
    
    recognition.start();
};

function sendSpeechToServer(speechResult) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/search_playlist", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            displayPlaylist(response.playlist_url);
        }
    };
    xhr.send(JSON.stringify({ query: speechResult }));
}

function fetchPlaylist(emotion) { // Accept the emotion parameter here
    fetch('/get_playlist', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ emotion: emotion })
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        // Open the playlist URL in a new tab
        window.open(data.playlist_url, '_blank');
      } else {
        console.error(data.message);
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function displayPlaylist(playlistUrl) {
    var playlistDiv = document.getElementById('playlistResult');
    playlistDiv.innerHTML = '<a href="' + playlistUrl + '" target="_blank">Spotify Playlist</a>';
}
