# pathsaver

A brew package for saving directory paths
Sure, here's a template for a README file for your package:

````
# Pathsaver

Pathsaver is a command-line tool for saving, listing, and deleting directory paths conveniently. It provides a simple way to save frequently used directory paths as variables, making it easier to navigate the file system in the terminal.

## Features

- Save directory paths with custom variable names
- List saved paths with their corresponding variable names
- Delete saved paths by variable name
- Delete all saved paths at once

## Installation

Pathsaver can be installed using Homebrew on macOS:

```bash
brew install TraXIcoN/pathsaver/pathsaver
````

## Usage

### Saving a Path

To save a directory path with a custom variable name:

```bash
pathsaver mydir /path/to/directory
```

### Listing Saved Paths

To list all saved paths and their corresponding variable names:

```bash
pathsaver --list
```

### Deleting a Saved Path

To delete a saved path by its variable name:

```bash
pathsaver --delete mydir
```

### Deleting All Saved Paths

To delete all saved paths:

```bash
pathsaver --delete-all
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

Feel free to customize the content to better fit your package's features, usage instructions, and contributing guidelines. Additionally, make sure to include relevant links, such as links to the GitHub repository, license file, and any other resources related to your package.
```
