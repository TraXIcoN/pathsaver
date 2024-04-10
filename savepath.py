#!/usr/bin/env python3

import os
import sys

# Define the path to the file where paths will be saved
SAVED_PATHS_FILE = os.path.expanduser('~/.saved_paths')

def save_path(variable_name, directory_path):
    with open(SAVED_PATHS_FILE, 'a') as f:
        f.write(f'export {variable_name}="{directory_path}"\n')
    print(f"Saved '{directory_path}' as variable '{variable_name}'")

def main():
    if len(sys.argv) < 2:
        print("Usage: savepath <variable_name> [directory_path]")
        sys.exit(1)

    variable_name = sys.argv[1]
    if len(sys.argv) > 2:
        directory_path = sys.argv[2]
    else:
        directory_path = os.getcwd()  # Use current directory if no path provided
    save_path(variable_name, directory_path)

if __name__ == "__main__":
    main()

