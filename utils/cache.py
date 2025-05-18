import os

_cache = {}

def get_cached_media(filename):
    if filename not in _cache:
        full_path = os.path.join("resources", filename)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Media file not found: {full_path}")

        with open(full_path, "rb") as f:
            content = f.read()

        if not content:
            raise ValueError(f"File {filename} is empty.")

        _cache[filename] = content

    return _cache[filename]  # return raw bytes only
