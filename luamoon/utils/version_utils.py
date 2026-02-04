def is_valid_version(version_str):
    parts = version_str.split('.')
    if len(parts) < 2:
        return False

    for part in parts:
        if not part.isdigit():
            return False

    return True
