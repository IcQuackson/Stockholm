
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div class="center-text">
    <h1 align="center">
    	🥷 Stockholm 🥷
    </h1>
    <h3 align="center">
      <i>
    	  Introduction to file manipulation by creating a ransomware.
      </i>
    </h3>
    <div align="center">
      <img alt="reverse" src="https://github.com/user-attachments/assets/852408dd-f029-4507-95eb-6bf89445ab1f" width=250px/>
      <p>The goal of this project is to write a program inspired by Wannacry that encrypts and decrypts file using a user provided key</p>
    </div>
  </div>

# Stockholm

Stockholm is a command-line program developed for **Linux** that encrypts (or decrypts) files located in the `infection` folder under a user's home directory. It uses a secure algorithm to protect or restore files that match certain extensions historically affected by WannaCry ransomware. 

---

## Table of Contents
1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Requirements](#requirements)
5. [Implementation Details](#implementation-details)
6. [Error Handling](#error-handling)
7. [License](#license)

---

## Features

- **Encrypt & Decrypt**: Encrypts files with a secure algorithm using a key of at least 16 characters, and decrypts them back using the same key.
- **File Renaming**: Automatically appends `.ft` to files after encryption unless they already have the `.ft` extension.
- **Silent Mode**: Optionally run without printing any output.
- **Error-Resistant**: Handles errors gracefully without unexpected termination.
- **Minimal & Focused**: Designed specifically for files in `~/infection` that match the known WannaCry-affected extensions.

---

## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/stockholm.git
    cd stockholm
    ```

2. **Build and start container**:
    ```bash
    make
    ```
3. **Connect to container and start using program**:
    ```bash
    make connect
    python3 main.py
    ```

---

## Usage

The program runs on **Linux** and requires you to have a folder named `infection` in your home directory, i.e., `~/infection`. It will only encrypt or decrypt the files affected by WannaCry within this folder.

### Command Options

```bash
stockholm [options]
```
- `-h, --help`: Displays the help screen (list of available options).
- `-v, --version`: Shows the current version of the program.
- `-r <key>, --reverse <key>`: Performs the reverse (decryption) operation using the provided key.
- `-s, --silent`: Runs the program without printing any file names or progress messages.

### Examples

1. **Encrypting files**:
    ```bash
    python3 main.py MY_LONG_SECURE_KEY
    ```
   This will encrypt all eligible files in `~/infection` with your prompted key, and append `.ft` to them.

2. **Decrypting (reverse)**:
    ```bash
    python3 main.py --reverse MY_LONG_SECURE_KEY
    ```
   This will decrypt previously encrypted files using the specified key.

3. **Silent run**:
    ```bash
    python3 main.py -s MY_LONG_SECURE_KEY
    ```
   This encrypts files but does not print any output to the terminal.

4. **Help**:
    ```bash
    python3 main.py --help
    ```

---

## Requirements

1. The project **must be developed for Linux**.
2. The program must handle the following options:
   - `--help` or `-h` to display help
   - `--version` or `-v` to display the program version
   - `--reverse` or `-r` to reverse the infection (decrypt) using a provided key
   - `--silent` or `-s` to suppress all output
3. The program must:
   - Work **only** in the `infection` directory located at `~/infection`
   - Target files with **extensions known to be affected by WannaCry** (research is required to confirm these)
   - Encrypt file contents using a **secure algorithm** (e.g., AES-256)
   - Rename files to add the `.ft` extension unless they already have it
   - Use a key **at least 16 characters long**
   - Be able to **reverse** the process to restore files using the same key
   - Gracefully handle errors and avoid unexpected stops

---

## Implementation Details

- **Encryption Algorithm**: Sha256 i sused to expand the key and then ChaCha20-Poly1305 is used through libsodium to encrypt the contents of the files.  
- **Key Management**:  
  - Ensure that the key length is **at least 16 characters**.  
  - Provide a method for users to supply the key.  
- **File Rename Logic**:  
  - After successfully encrypting a file, rename it to `filename.ext.ft`.  
  - If it already ends in `.ft`, do not rename.  
- **File Extensions**: Research the standard WannaCry-affected extensions (e.g., `.doc`, `.xls`, etc.). The program should only encrypt those file types.

**Directory Restriction**  
- The program should verify the files are within `~/infection` only. If the folder does not exist, it can create it or exit gracefully with an error message.  

---

## Error Handling

- If any file fails to encrypt or decrypt, print (or log, if silent mode is disabled) an error but **continue** with the next file.
- For invalid options or missing arguments:
  - Show a usage message and exit.
- If the key is missing or too short:
  - Print an error message and exit.
- If the encryption/decryption algorithm fails:
  - Print an error message and exit gracefully.

---

## License

This project is distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

> **Disclaimer**  
> This tool is strictly for educational and ethical testing purposes. Use responsibly and ensure you have the rights to encrypt/decrypt target files.
