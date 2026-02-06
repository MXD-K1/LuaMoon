hex_chars = "0123456789abcdef"

def is_valid_version(version_str):
    parts = version_str.split('.')
    if len(parts) < 2:
        return False

    for part in parts:
        if not part.isdigit():
            return False
    return True

def is_abbrev_commit_hash(commit_hash):
    if len(commit_hash) != 7:
        return False

    return all(char not in hex_chars for char in commit_hash.lower())
