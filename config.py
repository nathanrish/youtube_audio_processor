from dotenv import load_dotenv
import os

load_dotenv()

DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH")
OUTPUT_DIR = os.getenv("OUTPUT_DIR")
CHUNK_LENGTH_MS = int(os.getenv("CHUNK_LENGTH_MS"))
