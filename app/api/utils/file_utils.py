from .constants import BASE_DIR
import os

def get_file_path(filename: str) -> str:
    """Gets the file path."""
    return os.path.join(BASE_DIR, "files", filename)


def save_file(file: bytes, filename: str) -> None:
    """Saves a file."""
    file_path = get_file_path(filename)
    with open(file_path, "wb") as f:
        f.write(file)
