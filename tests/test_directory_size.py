import os
import pytest
import tempfile
from src.directory_size import calculate_directory_size

def test_calculate_directory_size():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with known sizes
        files = [
            ('file1.txt', 100),
            ('file2.txt', 250),
            ('subdir/file3.txt', 75)
        ]
        
        # Create files with specified sizes
        for file_path, size in files:
            full_path = os.path.join(temp_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'wb') as f:
                f.write(b'0' * size)
        
        # Calculate total size and verify
        total_size = calculate_directory_size(temp_dir)
        assert total_size == sum(size for _, size in files)

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        calculate_directory_size('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file instead of a directory
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            calculate_directory_size(temp_file.name)

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert calculate_directory_size(temp_dir) == 0