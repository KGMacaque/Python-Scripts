


#   PythonMediaFileRenamingScript.py
*Specifically Taylored for Video Files (i.e., TV Shows). But works on any filename.*

## Description

This Python script renames media files in a specified directory by replacing dots (`.`) and underscores (`_`) with spaces, capitalizing words with more than three characters, and removing any characters after the "SxxExx" term. It also includes a verbose mode for detailed output and an option to revert changes if they are not acceptable.

## Features

1. **Replace Characters**:
   - Replaces dots (`.`) and underscores (`_`) in filenames with spaces (` `).

2. **Capitalize Words**:
   - Capitalizes words with more than three characters.

3. **Regular Expression**:
   - Removes characters after the "SxxExx" term using a regular expression.

4. **Verbose Mode**:
   - Prints old and new filenames during the renaming process when enabled.

5. **Revert Changes**:
   - Provides an option to revert filenames to their original state if the changes are not acceptable.

## Usage

1. **Clone the Repository**:

          git clone https://github.com/KGMacaque/Python-Media-File-Renaming-Script.git

3. **Move into Directory**

          cd Python-Media-File-Renaming-Script

4. **Run the Script:**

          python PythonMediaFileRenamingScript.py

5. **Follow the Prompts:**
   
   -  When asked, input the directory location containing the files to be renamed.
   -  Enable verbose output, if desired `(yes,no)`, `(y,n)`.
   -  Review the changes and indicate whether they are acceptable `(yes,no)`, `(y,n)`.


#   Example

    Original Filename:

        my_file.S01E01.example_file.ext

    Renamed Filename:

        My File S01E01.ext


Verbose Output *(if enabled)*:

     Renaming: my_file.S01E01.example_file.ext ---> My File S01E01.ext

     Files Have Been Renamed *or* Reverting Changes (if not acceptable):

     Changes have been reverted.




##  Code Overview

#   Functions

    rename_files(directory, verbose=False)
        Renames files according to specified rules and returns a list of renamed files.

    revert_filenames(directory, renamed_files)
        Reverts filenames to their original names.

#   Main Function

    main()
        Handles user interaction and orchestrates the renaming and reverting processes.

#   Dependencies

    Python 3.x

#   Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.

#   License

This project is licensed under the MIT License. See the LICENSE file for details.

#   Author

    KGMacaque

#   Acknowledgements

    Special thanks to all contributors and the Python community for their support.



*Feel free to modify the content as necessary to fit your specific need*
