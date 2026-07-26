# Password Manager

A simple command-line password manager written in Python. It lets you save, view, and generate passwords, storing them locally in a text file.

## Features

- **Save a password** — Store a password for a given website/service.
- **View saved passwords** — List all previously saved website/password pairs.
- **Generate a password** — Create a random 8-character password using letters, digits, and punctuation.
- **Persistent storage** — Saved passwords are written to `passwords.txt` so they're available the next time you run the program.

## Requirements

- Python 3.x (no external dependencies — uses only the built-in `random` and `string` modules)

## Installation

```bash
git clone https://github.com/Jit2005git/password_manager.git
cd password_manager
```

## Usage

Run the script:

```bash
python password_manager.py
```

You'll see a menu:

```
------ Password Manager ------
1. Save password
2. View existing passwords
3. Generate a new password
4. Exit
```

- **1 — Save password**: Enter a website name and a password to store it.
- **2 — View existing passwords**: Prints all saved website/password pairs.
- **3 — Generate a new password**: Generates and displays a random 8-character password (not saved automatically).
- **4 — Exit**: Closes the program.

## How it works

- Passwords are stored in `passwords.txt` in the format `website:password`, one entry per line.
- On startup, the script loads any existing entries from `passwords.txt` into memory.
- New entries are appended to the file whenever you save a password.

## ⚠️ Security Note

This project stores passwords in **plain text** in `passwords.txt` — nothing is encrypted or hashed. It's intended as a learning project / basic utility, **not** a secure way to store real, sensitive passwords. If you plan to use something like this for real accounts, consider adding encryption (e.g. via the `cryptography` library) before storing any data.

## License

No license specified yet. Consider adding one (e.g. MIT) if you plan to share or accept contributions to this project.

