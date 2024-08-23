import librosa
import noisereduce as nr

def clean_audio(file_path):
    y, sr = librosa.load(file_path, sr=None)
    reduced_noise = nr.reduce_noise(y=y, sr=sr)
    return reduced_noise, sr
