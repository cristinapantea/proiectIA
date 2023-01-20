import librosa
import time
import os

filename = librosa.example('pistachio')
file = os.path.join('Frank-Sinatra-Jingle-Bells.wav')
y, sr = librosa.load(file)
duration = librosa.get_duration(y=y, sr=sr)
print('Durata melodiei:', time.strftime("%H:%M:%S", time.gmtime(duration)))
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
