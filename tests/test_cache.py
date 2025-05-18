import os
import pytest
from utils.cache import get_cached_media

def test_cached_media_loads_correctly(tmp_path, monkeypatch):
    # Create a dummy file in the temp directory
    filename = "dummy.txt"
    expected_bytes = b"test data"
    dummy_file = tmp_path / filename
    dummy_file.write_bytes(expected_bytes)

    # Monkeypatch os.path.join to redirect to our dummy file
    monkeypatch.setattr(os.path, "join", lambda *args: str(dummy_file))

    # Now this will read from tmp_path instead of resources/
    result = get_cached_media(filename)

    assert result == expected_bytes

def test_cached_media_is_not_zero_bytes(tmp_path, monkeypatch):
    # Step 1: Create a known test file
    filename = "video.mp4"
    content = b"\x00\x01\x02\x03\x04" * 100  # 500 bytes of binary data
    file_path = tmp_path / filename
    file_path.write_bytes(content)

    # Step 2: Patch os.path.join so the cache function reads our test file
    monkeypatch.setattr(os.path, "join", lambda *_: str(file_path))

    # Step 3: Call the function twice
    first = get_cached_media(filename)
    second = get_cached_media(filename)

    # Step 4: Assert both are correct and not empty
    assert len(first) == 500, "First load returned incorrect size"
    assert len(second) == 500, "Second load returned incorrect size"
    assert first == second, "Subsequent cache access returned different content"
