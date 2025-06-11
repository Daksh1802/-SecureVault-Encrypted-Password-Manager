# 🔐 SecureVault – Command-Line Password Manager

SecureVault is a beginner-friendly, command-line based password manager written in Python. It demonstrates secure password handling using salted hashing and AES encryption with Fernet.

---

## ✨ Features

- 🔐 **User Authentication**
  - SHA-256 hashing with per-user salt for secure master password storage
  - Local storage of hashed credentials in JSON format

- 🧠 **Credential Management**
  - Add and view credentials for websites
  - Credentials are AES-encrypted using `cryptography.fernet`
  - Each credential uses a unique encryption key

- 📂 **Per-User Credential Storage**
  - Each user has isolated storage for credentials and encryption keys

- 🖥️ **Simple CLI Interface**
  - Easy-to-use terminal prompts for all operations

---

## 🗂 File Structure

```text
.
├── securevault.py             # Main application script
├── Mastercred.json            # Stores salted and hashed master passwords
├── <username>cred.json        # Encrypted user credentials
├── <username>keys.json        # Encryption keys per website
├── README.md                  # Project documentation
🚀 Getting Started
Prerequisites
Python 3.7+

Install the required package:

bash
Copy
Edit
pip install cryptography
Running the App
bash
Copy
Edit
python securevault.py
Follow the on-screen instructions to sign up or sign in, then add or view credentials.

🛡️ Security Measures
Mechanism	Description
SHA-256 + Salt	Securely hashes master passwords with a unique salt
Fernet Encryption	AES-128 encryption of credentials
File Separation	Separate files for hashed credentials and encryption keys

⚠️ Note: This tool is for educational purposes only and not production-ready. For real-world applications, consider integrating secure key vaults and user authentication libraries.

📌 Future Improvements
GUI interface

Password strength checker

Secure key vault (e.g., HashiCorp Vault, AWS KMS)

Brute-force protection and attempt logging

👨‍💻 Author
Made by Daksh Perswal
https://github.com/Daksh1802
