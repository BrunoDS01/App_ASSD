import pytube
import numpy as np
import librosa

#############################################################################
# Download Youtube Audio
#############################################################################
def downloadYoutubeAudio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '44100',
        }],
        'outtmpl': '%(title)s.wav',
    }

    yt = pytube.YouTube(url)

    streams = yt.streams.filter(only_audio = True).all()
    
    for i in range(len(streams)):
        streams[i].download(filename= str(i) + ".mp3")
    
    audio = np.zeros(0)

    for i in range(len(streams)):
        aux, sr = librosa.load(str(i) + ".mp3")
        audio = np.concatenate((audio, aux), axis=0)

    return audio, 44100