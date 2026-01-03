# 🛡️ Python File Shield (AES-256 Encryption)

A lightweight Backend tool built in Python to secure sensitive files using Fernet (symmetric encryption). This tool can encrypt and decrypt any file type (Images, PDFs, Text) by handling raw binary data.

## ✨ Features
- **Symmetric Encryption:** Uses the `cryptography` library for high-security file locking.
- **Binary Support:** Works on any file format (not just .txt).
- **Key Management:** Automatically generates and manages a `secret.key` file.
- **Safe I/O:** Implements a read-process-write pattern to prevent file corruption.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Library:** `cryptography` (Fernet)
- **Concepts:** File I/O, Error Handling, Binary Data Manipulation.

## 🚀 How to Run
1. Clone the repo: `git clone <your-repo-link>`
2. Install dependencies: `pip install cryptography`
3. Run the script: `python main.py`