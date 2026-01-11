# File Shield 🛡️

A professional-grade file security utility built in Python. This tool provides robust AES-256 encryption using password-based key derivation (PBKDF2), allowing users to secure individual files or entire directories with a single master password.

## 🚀 Key Features
- **Password-Based Security:** Uses **PBKDF2** (Password-Based Key Derivation Function 2) with 100,000 iterations to generate secure keys.
- **Symmetric Encryption:** Leverages the industry-standard `cryptography.fernet` (AES) implementation.
- **Bulk Processing:** Intelligently identifies and processes every file within a directory while ignoring system-critical files like the salt.
- **Safety Guard:** Implements logic to skip sub-directories and the encryption salt to prevent accidental data loss.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Library:** `cryptography`
- **Focus Areas:** Information Technology, Cybersecurity, File I/O.

## ⚙️ How to Use
1. **Setup:** Ensure you have the cryptography library installed:
   ```bash
   pip install cryptography
2. **Run:** Execute main.py and enter a Master Password.

3. **Target:** Provide a file path (e.g., my_notes.txt) or a folder path (e.g., ./secret_docs/).

4. **Action:** Choose (1) to lock or (2) to unlock.

## ⚠️ Important Security Note
This tool relies on the X.salt file.

DO NOT delete X.salt.

DO NOT share your Master Password. If either is lost, the data is mathematically impossible to recover.

Developed as part of my BTech IT Portfolio.