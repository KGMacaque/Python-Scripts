 
#!/usr/bin/env python3

#############################
######  Created By: KGMacaque   ######
#############################

import os
import re


def replace_characters(filename):
    """Replaces dots and underscores with spaces in the filename."""
    return filename.replace('.', ' ').replace('_', ' ')


def capitalize_words(filename):
    """Capitalizes words with more than 3 characters."""
    words = filename.split()
    capitalized_words = [word.capitalize() if len(word) > 3 else word for word in words]
    return ' '.join(capitalized_words)


def ensure_uppercase_pattern(filename):
    """Ensures the SXXEXX pattern is uppercase."""
    match = re.search(r'(S\d{2}E\d{2})', filename, re.IGNORECASE)
    if match:
        pattern = match.group(0).upper()  # Ensure the pattern is uppercase
        return filename[:match.start()] + pattern + filename[match.end():]
    return filename  # Return original filename if no pattern found


def add_hyphen_before_pattern(filename):
    """Adds a hyphen and space before the SXXEXX pattern (if present)."""
    match = re.search(r'(S\d{2}E\d{2})', filename, re.IGNORECASE)
    if match:
        before_pattern = filename[:match.start()].rstrip()
        if not before_pattern.endswith('-'):
            before_pattern += ' -'
        return before_pattern + ' ' + filename[match.start():]
    return filename  # Return original filename if no pattern found


def remove_extra_characters(filename):
    """Removes characters after the SXXEXX pattern (if present)."""
    match = re.search(r'(S\d{2}E\d{2})', filename, re.IGNORECASE)
    if match:
        return filename[:match.end()]  # Keep only characters up to the pattern
    return filename  # Return original filename if no pattern found


def rename_files(directory, verbose=True):
    """Renames files in a directory with transformations."""
    original_filenames = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if os.path.isfile(os.path.join(root, filename)):
                base, ext = os.path.splitext(filename)

                # Apply transformations sequentially
                new_filename = replace_characters(base)
                new_filename = capitalize_words(new_filename)
                new_filename = ensure_uppercase_pattern(new_filename)
                new_filename = add_hyphen_before_pattern(new_filename)
                new_filename = remove_extra_characters(new_filename) + ext

                original_filenames[os.path.join(root, new_filename)] = os.path.join(root, filename)

                if verbose:
                    print(f'Renaming: {filename} ---> {new_filename}')

                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))

    return original_filenames


def revert_changes(original_filenames):
    """Reverts changes made by rename_files."""
    for new_path, original_path in original_filenames.items():
        try:
            os.rename(new_path, original_path)
        except FileNotFoundError:
            print(f"Warning: Could not revert {new_path}. Original file not found.")

def main():
    directory = "ENTER*DIRECTORY*PATH*HERE>"  # Set the directory here
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    original_filenames = rename_files(directory)

    accept_changes = input('Are the changes acceptable? (yes,no) (y,n): ').strip().lower()
    if accept_changes not in ['yes', 'y']:
        revert_changes(original_filenames)
        print('Changes have been reverted.')
    else:
        print('Files have been renamed.')

if __name__ == '__main__':
    main()
