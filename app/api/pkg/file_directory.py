from pathlib import Path

def get_file_directory():
    UPLOAD_DIRECTORY = Path(__file__).resolve().parent.parent.parent.parent / "media/images"
    UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)
    return UPLOAD_DIRECTORY
