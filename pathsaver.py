#!/usr/bin/env python3

import os
import sys
import argparse
from tabulate import tabulate
import argcomplete

# Define the path to the file where paths will be saved
SAVED_PATHS_FILE = os.path.expanduser('~/.saved_paths')

def save_path(variable_name, directory_path):
    with open(SAVED_PATHS_FILE, 'a') as f:
        f.write(f'export {variable_name}="{directory_path}"\n')
    print(f"Saved '{directory_path}' as variable '{variable_name}'")

def list_saved_paths():
    paths = []
    with open(SAVED_PATHS_FILE, 'r') as f:
        for line in f:
            if line.startswith("export"):
                parts = line.strip().split("=")
                variable_name = parts[0].split()[1]
                directory_path = parts[1].strip('"')
                paths.append((variable_name, directory_path))
    return sorted(paths)

def delete_path(variable_name):
    with open(SAVED_PATHS_FILE, 'r') as f:
        lines = f.readlines()
    with open(SAVED_PATHS_FILE, 'w') as f:
        for line in lines:
            if not line.startswith(f'export {variable_name}'):
                f.write(line)
    print(f"Deleted path with variable name '{variable_name}'")

def delete_all_paths():
    if os.path.exists(SAVED_PATHS_FILE):
        with open(SAVED_PATHS_FILE, 'w') as f:
            f.truncate(0)
        print("All saved paths have been deleted.")
    else:
        print("No saved paths to delete.")

def get_variable_names():
    variable_names = []
    with open(SAVED_PATHS_FILE, 'r') as f:
        for line in f:
            if line.startswith("export"):
                parts = line.strip().split("=")
                variable_name = parts[0].split()[1]
                variable_names.append(variable_name)
    return variable_names

def main():
    parser = argparse.ArgumentParser(description="Save, list, and delete paths")
    parser.add_argument("variable_name", nargs="?", help="Name of the variable to save/delete").completer = lambda *args: get_variable_names()
    parser.add_argument("directory_path", nargs="?", help="Directory path to save", default=os.getcwd())
    parser.add_argument("--list", action="store_true", help="List saved paths")
    parser.add_argument("--delete", action="store_true", help="Delete a saved path by variable name")
    parser.add_argument("--delete-all", action="store_true", help="Delete all saved paths")

    argcomplete.autocomplete(parser)

    args = parser.parse_args()

    if args.list:
        saved_paths = list_saved_paths()
        if saved_paths:
            print("Saved Paths:")
            print(tabulate(saved_paths, headers=["Variable Name", "Directory Path"], tablefmt="grid"))
        else:
            print("No paths saved.")
    elif args.variable_name and args.delete:
        delete_path(args.variable_name)
    elif args.delete_all:
        delete_all_paths()
    elif args.variable_name:
        save_path(args.variable_name, args.directory_path)
    else:
        parser.print_help(sys.stderr)

if __name__ == "__main__":
    main()

