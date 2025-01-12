import re

def str_to_safe_filename(original_string):
    # Replace spaces with underscores or hyphens (choose one)
    safe_string = original_string.replace(" ", "_")  # or use .replace(" ", "-")

    # Remove any characters that are not alphanumeric, underscores, or hyphens
    safe_string = re.sub(r'[^\w\-]', '', safe_string)

    # Optionally, make the filename lowercase for consistency
    safe_string = safe_string.lower()

    return safe_string