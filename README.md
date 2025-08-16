# TwinCrypt 🔐

TwinCrypt is a Python-based desktop application that lets you **encrypt and decrypt text using a two-layer cipher system**:

1. **Vigenère Cipher** – A classical polyalphabetic substitution cipher.
2. **One-Time Pad (OTP)** – A theoretically unbreakable cipher that uses a random key.

By combining them, TwinCrypt adds **an extra layer of security** while keeping things simple with an intuitive **Tkinter GUI**.

---

## ✨ Features

* 🔒 **Dual Encryption**: Encrypts text first with Vigenère, then with a random OTP.
* 🔑 **Secure Key Handling**: Saves the OTP key to `otp_key.txt` for safe sharing.
* 🔁 **Easy Decryption**: Just provide the ciphertext, OTP key, and Vigenère key to get back the original text.
* 🖥️ **User-Friendly GUI**: Large font, clean layout, and simple buttons for encrypt/decrypt.
* ⚡ **Cross-Platform**: Runs anywhere Python and Tkinter are available.

---

## 🚀 How It Works

### 🔐 Encryption Flow

```
Plaintext → Vigenère Encrypt → OTP Encrypt → Final Ciphertext
```

### 🔓 Decryption Flow

```
Final Ciphertext → OTP Decrypt → Vigenère Decrypt → Plaintext
```

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/TwinCrypt.git
cd TwinCrypt
python app.py
```

---

## 🎯 Use Cases

* Learning classical cryptography
* Demonstrating how layered encryption works
* Secure message sharing (with proper OTP key exchange)

---

## 📸 Screenshot

https://ibb.co/93TZVsVY

---

## ⚠️ Disclaimer

This project is for **educational purposes**.
While OTP is secure in theory, practical key-sharing and storage challenges mean you should not use this tool for serious security needs.

---

## 🏷️ Suggested Topics

`python, cryptography, encryption, decryption, cipher, vigenere-cipher, one-time-pad, otp, tkinter, desktop-application, educational`
