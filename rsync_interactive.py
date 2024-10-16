#!/usr/bin/env python3

import os
import subprocess


def get_yes_no(prompt):
    while True:
        response = input(prompt + " (yes/no): ").strip().lower()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']  # Return True if 'yes' or 'y'
        print("Please enter 'yes', 'y', 'no', or 'n'.")


def get_exclude_patterns():
    patterns = []
    while True:
        pattern = input("Enter a pattern to exclude (or leave blank to finish): ").strip()
        if not pattern:
            break
        patterns.append(pattern)
    return patterns


def main():
    # Define the available options
    options = {
        '--checksum': "skip based on checksum, not mod-time & size",
        '--archive': "archive mode is -rlptgoD (no -A,-X,-U,-N,-H)",
        '--safe-links': "ignore symlinks that point outside the tree",
        '--delete': "delete extraneous files from destination directory(s)",
        '--remove-source-files': "sender removes synchronized [source] files (non-directory(s))",
        '--append': "append data onto shorter files",
        '--dry-run': "perform a trial run with no changes made",
    }

    # Ask the user for rsync options
    selected_options = []
    for option, description in options.items():
        if get_yes_no(f"Do you want to use {option}? ({description})"):
            selected_options.append(option)

    # Ask if the user wants to exclude patterns
    if get_yes_no("Do you want to use --exclude=PATTERN?"):
        exclude_patterns = get_exclude_patterns()
        for pattern in exclude_patterns:
            selected_options.append(f"--exclude={pattern}")

    # Always appended options
    always_appended_options = [
        '--stats',
        '--info=all',
        '--partial',
        '--itemize-changes',
        '--compress',
        '--progress',
        '--human-readable'
    ]
    selected_options.extend(always_appended_options)

    # Ask for source and destination directories
    source = input("Please enter the source directory: ").strip()  # Add trailing slash
    destination = input("Please enter the destination directory: ").strip()

    # Create the log file path
    log_file = os.path.join(destination, 'log.txt')

    # Append to the log file
    selected_options.append(f"--log-file={log_file}")

    # Construct the rsync command
    rsync_command = ['rsync'] + selected_options + [source, destination]

    # Run the rsync command
    print(f"Running command: {' '.join(rsync_command)}")
    result = subprocess.run(rsync_command, capture_output=True, text=True)

    # Output the result
    print(result.stdout)
    print(result.stderr)


if __name__ == "__main__":
    main()
