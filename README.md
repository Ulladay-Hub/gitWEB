# GitWEB

GitWEB is a lightweight version control system designed for managing websites and database schemas, written in Rust. This repository provides essential functionalities similar to Git, tailored for web development and database management projects.

## Features

- **Repository Initialization**: Initialize a `.git_web` directory structure to start tracking changes.
  
- **Commit Management**: Create commits with messages and descriptions to track changes in HTML, CSS, JavaScript, and database schemas.

- **Blame View Port (BVP)**: View commit histories and associated messages to understand who made changes and when.

## Installation

To use GitWEB locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ulladay-Hub/gitweb.git
   cd gitweb
   ```

2. **Initialize GitWEB Repository**:
   Run `dir_init.py` to initialize the `.git_web` directory structure:
   ```bash
   python dir_init.py
   ```

3. **Create a New Commit**:
   Use `commit.py` to create a new commit with a message and description:
   ```bash
   python commit.py
   ```

## Usage

### Initializing the Repository

To initialize a GitWEB repository:

```bash
python dir_init.py
```

This command will create a `.git_web` directory structure in your current working directory.

### Creating a Commit

To create a new commit:

```bash
python commit.py
```

Follow the prompts to enter a commit message and description. This will create a new commit with a unique commit ID under `.git_web/commits`.

### Viewing Commit History

Explore commit histories and messages using the BVP (Blame View Port). This feature allows you to track changes and understand the evolution of your website and database schemas over time.

## Structure

- **.git_web/**: Main directory for GitWEB repository.
  - **commits/**: Directory to store commit data.
    - Each commit is stored in a subdirectory named after its commit ID.
    - Contains `commit_message.txt` with commit details and a placeholder `<commit_id>.zip` file.

## Contributing

Contributions to GitWEB are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Or if you want, become part of the project, just leave a message in a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, feel free to contact [imnotamilkglass@gmail.com](mailto:imnotamilkglass@gmail.com).

GitHub: [Ulladay-Hub](https://github.com/Ulladay-Hub)

## Acknowledgements

- Built with Python programming language.
- Inspired by Git version control system.
