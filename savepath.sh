#!/bin/bash

# Execute the Python script to save the path
python3 ./savepath.py "$@"

# Load saved paths into the current shell session
load_saved_paths() {
    local saved_paths_file="$HOME/.saved_paths"
    if [ -f "$saved_paths_file" ]; then
        while IFS= read -r line; do
            eval "$line"
        done < "$saved_paths_file"
    fi
}

# Call the function to load saved paths
load_saved_paths

