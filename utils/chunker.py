import os
import librosa
import soundfile as sf

def chunk_audio(audio, sr, chunk_length_ms=5000):
    chunk_length = int(sr * (chunk_length_ms / 1000))
    chunks = [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]
    return chunks

def save_chunks(chunks, sr, output_dir='audio_chunks'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, chunk in enumerate(chunks):
        chunk_file = os.path.join(output_dir, f'chunk_{i}.wav')
        sf.write(chunk_file, chunk, sr)  # Save the chunk using soundfile
