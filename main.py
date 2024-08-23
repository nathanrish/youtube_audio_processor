from utils.downloader import download_youtube_video
from utils.processor import clean_audio
from utils.chunker import chunk_audio, save_chunks
import config

def main():
    # Ask for YouTube URL
    youtube_url = input("Enter the YouTube video URL: ")

    # Step 1: Download YouTube video and extract audio
    audio_file = download_youtube_video(youtube_url, config.DOWNLOAD_PATH)

    # Step 2: Load and clean audio
    cleaned_audio, sr = clean_audio(audio_file)

    # Step 3: Split audio into chunks
    audio_chunks = chunk_audio(cleaned_audio, sr, config.CHUNK_LENGTH_MS)

    # Step 4: Save chunks to files
    save_chunks(audio_chunks, sr, config.OUTPUT_DIR)

    print(f"Audio processing complete. Chunks saved to {config.OUTPUT_DIR}")

if __name__ == "__main__":
    main()
