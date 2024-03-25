from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']

    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(os.path.expanduser("~/Downloads"))  # Descargar en la carpeta de descargas del usuario
        return ''
    except Exception as e:
        return f'Ocurrió un error al intentar descargar el video: {e}'

if __name__ == '__main__':
    app.run(debug=True)
