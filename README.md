
# YouTube Audio Processor

**YouTube Audio Processor** is a tool designed for downloading YouTube videos, extracting and cleaning audio, and splitting the audio into chunks. It's useful for creating high-quality audio datasets for training Text-to-Speech (TTS) models and other audio-based applications.

## Features

- **Download Audio**: Fetch audio from YouTube videos using `yt-dlp`.
- **Noise Reduction**: Remove background noise with `noisereduce`.
- **Audio Processing**: Analyze and process audio using `librosa` and `pydub`.
- **Audio Chunking**: Split audio into smaller chunks.

## Project Structure

```
youtube_audio_processor/
│
├── main.py               # Main script to run the process
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignore rules
├── .env                  # Environment variables (optional)
│
├── utils/                # Utility scripts
│   ├── downloader.py     # For downloading audio from YouTube
│   ├── processor.py      # For cleaning audio
│   └── chunker.py        # For splitting audio into chunks
│
└── audio_chunks/         # Directory for saving audio chunks
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nathanrish/youtube_audio_processor.git
   cd youtube_audio_processor
   ```

2. **Set Up the Environment**

   Create and activate a virtual environment (optional but recommended):

   ```bash
   conda create --name youtube_audio_processor python=3.8
   conda activate youtube_audio_processor
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory if you need to use environment variables. Example configuration:

```
# .env file
DOWNLOAD_PATH=downloads
OUTPUT_DIR=audio_chunks
CHUNK_LENGTH_MS=5000
```

## Usage

1. **Run the Main Script**

   Execute the `main.py` script. You will be prompted to enter the YouTube video URL:

   ```bash
   python main.py
   ```

2. **Enter the YouTube URL**

   When prompted, provide the URL of the YouTube video you want to process:

   ```
   Enter the YouTube video URL: https://youtu.be/your_video_id
   ```

3. **Results**

   - The audio will be downloaded and saved in the `DOWNLOAD_PATH`.
   - The audio will be cleaned and split into chunks.
   - The processed chunks will be saved in the `OUTPUT_DIR`.

## Code Examples

**Downloader (`utils/downloader.py`):**

```python
import os
from yt_dlp import YoutubeDL

def download_youtube_video(url, download_path='downloads'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
        return filename.replace('.webm', '.wav').replace('.mp4', '.wav')
```

**Processor (`utils/processor.py`):**

```python
import noisereduce as nr
import librosa

def clean_audio(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    cleaned_audio = nr.reduce_noise(y=audio, sr=sr)
    return cleaned_audio, sr
```

**Chunker (`utils/chunker.py`):**

```python
import os
import soundfile as sf

def chunk_audio(audio, sr, chunk_length_ms=5000):
    chunk_length = int(sr * (chunk_length_ms / 1000))
    return [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]

def save_chunks(chunks, sr, output_dir='audio_chunks'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, chunk in enumerate(chunks):
        chunk_file = os.path.join(output_dir, f'chunk_{i}.wav')
        sf.write(chunk_file, chunk, sr)
```

## Troubleshooting

- **HTTP Error 400**: Check if the URL is correct and ensure `yt-dlp` is up to date.
- **Missing Libraries**: Make sure all dependencies are installed by running `pip install -r requirements.txt`.

## Contributing

Contributions are welcome! Fork the repository and submit pull requests. For major changes, open an issue to discuss the modifications before creating a PR.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

