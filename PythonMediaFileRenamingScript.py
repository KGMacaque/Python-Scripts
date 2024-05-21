                         
                                            ######################################
                                            ######  Created By: KGMacaque   ######
                                            ######################################

import os
import re

def rename_files(directory, verbose=False):
    renamed_files = []
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Extract the filename and extension
            name, extension = os.path.splitext(filename)
            
            # Replace dots with spaces
            name = name.replace('.', ' ')
            
            # Replace underscores with spaces
            name = name.replace('_', ' ')
            
            # Capitalize words with more than three characters
            name = ' '.join([word.capitalize() if len(word) > 3 else word for word in name.split()])
            
            # Remove characters after "SxxExx" term
            name = re.sub(r'(S\d{2}E\d{2}).*', r'\1', name, flags=re.IGNORECASE)
            
            # Construct the new filename
            new_filename = f"{name}{extension}"
            
            # Print the old and new filenames if verbose is enabled
            if verbose:
                print(f"Renaming: {filename} ---> {new_filename}")
            
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            
            # Store the original and new filenames
            renamed_files.append((filename, new_filename))
    
    return renamed_files

def revert_filenames(directory, renamed_files):
    # Revert the filenames to their original names
    for old_name, new_name in renamed_files:
        os.rename(os.path.join(directory, new_name), os.path.join(directory, old_name))

def main():
    # Ask the user for the directory containing the files.
    directory = input("Please enter the directory to work in: ")
    
    # Ask the user if they want verbose output
    verbose_input = input("Enable verbose output? (yes/no): ").strip().lower()
    verbose = verbose_input in ['yes', 'y']
    
    # Check if the directory exists
    if os.path.isdir(directory):
        # Call the rename function with verbose option
        renamed_files = rename_files(directory, verbose)
        print("Files have been renamed successfully.")
        
        # Ask the user if the changes are acceptable
        accept_changes = input("Are the changes acceptable? (yes/no): ").strip().lower()
        if accept_changes not in ['yes', 'y']:
            # Revert the changes if not acceptable
            revert_filenames(directory, renamed_files)
            print("Changes have been reverted.")
        else:
            print("Changes have been accepted.")
    else:
        print("The specified directory does not exist.")

if __name__ == "__main__":
    main()
