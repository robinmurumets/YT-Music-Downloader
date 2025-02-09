from flask import Flask, request, jsonify
from flask_cors import CORS
from pytubefix import YouTube
import os

app = Flask(__name__)
CORS(app)

@app.route('/download_audio', methods=['POST'])
def download_audio_endpoint():
    data = request.get_json()
    url = data.get('url')
    destination = data.get('destination', '.')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        if audio is None:
            return jsonify({'error': f"No audio stream found for {url}"}), 400

        song_path = audio.download(output_path=destination)
        base, ext = os.path.splitext(song_path)
        new_file = base + '.mp3'
        os.rename(song_path, new_file)
        return jsonify({'message': f"{yt.title} has been successfully downloaded as {new_file}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
