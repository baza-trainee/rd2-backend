"""File validation module."""


def file_valid(upload_file):
    """Check file is valid."""
    if not upload_file.filename.endswith('.pdf'):
        return False

    max_length = 2 * 1024 ** 2
    if (upload_file.size / 1024 ** 2) > max_length:
        return None

    return True
