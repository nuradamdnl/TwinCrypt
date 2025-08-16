import tkinter as tk
from tkinter import messagebox
import secrets
import string
from tkinter import font

# Function to generate a Vigenère key by repeating it to match the length of the message


def generate_vigenere_key(msg, keyword):
    return (keyword * (len(msg) // len(keyword))) + keyword[:len(msg) % len(keyword)]

# Function to generate a random One-Time Pad key of the same length as the ciphertext


def generate_otp_key(msg):
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(len(msg)))

# Vigenère cipher encryption


def encrypt_vigenere(msg, key):
    encrypted_text = []
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr(
                (ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr(
                (ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

# Vigenère cipher decryption


def decrypt_vigenere(msg, key):
    decrypted_text = []
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr(
                (ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr(
                (ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

# OTP encryption/decryption


def apply_otp(msg, key):
    result_text = []
    for i in range(len(msg)):
        result_char = chr(ord(msg[i]) ^ ord(key[i]))
        result_text.append(result_char)
    return "".join(result_text)

# GUI Functions


def encrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    vigenere_key = vigenere_key_entry.get().strip()
    if not text or not vigenere_key:
        messagebox.showerror(
            "Error", "Please provide text and a Vigenère key for encryption.")
        return

    # Step 1: Encrypt using Vigenère cipher
    vigenere_key_full = generate_vigenere_key(text, vigenere_key)
    vigenere_encrypted = encrypt_vigenere(text, vigenere_key_full)

    # Step 2: Encrypt the Vigenère ciphertext with OTP
    otp_key = generate_otp_key(vigenere_encrypted)
    otp_encrypted = apply_otp(vigenere_encrypted, otp_key)

    # Show the output
    output_text.delete("1.0", tk.END)
    output_text.insert(
        tk.END,
        f"Vigenere ciphertext: {vigenere_encrypted}\nFinal Ciphertext: {otp_encrypted}\nOTP Key (for Decryption): {otp_key}\n"
    )

    # Save OTP key to file
    with open("otp_key.txt", "w") as key_file:
        key_file.write(otp_key)
    messagebox.showinfo(
        "Key Saved", "The OTP key has been saved to 'otp_key.txt'. Please share it securely!")


def decrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    otp_key = otp_key_entry.get().strip()
    vigenere_key = vigenere_key_entry.get().strip()

    if not text or not otp_key or not vigenere_key:
        messagebox.showerror(
            "Error", "Please provide ciphertext, the OTP key, and the Vigenère key for decryption.")
        return

    # Step 1: Decrypt using OTP
    otp_decrypted = apply_otp(text, otp_key)

    # Step 2: Decrypt the resulting Vigenère ciphertext
    vigenere_key_full = generate_vigenere_key(otp_decrypted, vigenere_key)
    decrypted_text = decrypt_vigenere(otp_decrypted, vigenere_key_full)

    # Show the output
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Decrypted Text: {decrypted_text}")


# GUI setup
root = tk.Tk()
root.title("TwinCrypt")

# Global font
default_font = font.Font(family="Helvetica", size=20)

# Input text
tk.Label(root, text="Input Text:", font=default_font).grid(
    row=0, column=0, padx=20, pady=10, sticky="w")
input_text = tk.Text(root, height=5, width=60, font=default_font)
input_text.grid(row=0, column=1, padx=20, pady=10)

# Vigenère key entry
tk.Label(root, text="Vigenère Key:", font=default_font).grid(
    row=1, column=0, padx=20, pady=10, sticky="w")
vigenere_key_entry = tk.Entry(root, width=60, font=default_font)
vigenere_key_entry.grid(row=1, column=1, padx=20, pady=10)

# OTP key entry
tk.Label(root, text="OTP Key (for Decryption Only):", font=default_font).grid(
    row=2, column=0, padx=20, pady=10, sticky="w")
otp_key_entry = tk.Entry(root, width=60, font=default_font)
otp_key_entry.grid(row=2, column=1, padx=20, pady=10)

# Buttons
encrypt_button = tk.Button(
    root, text="Encrypt", command=encrypt_message, font=default_font)
encrypt_button.grid(row=3, column=0, padx=20, pady=20, sticky="w")

decrypt_button = tk.Button(
    root, text="Decrypt", command=decrypt_message, font=default_font)
decrypt_button.grid(row=3, column=1, padx=20, pady=20, sticky="w")

# Output text
tk.Label(root, text="Output:", font=default_font).grid(
    row=4, column=0, padx=20, pady=10, sticky="w")
output_text = tk.Text(root, height=8, width=60, font=default_font)
output_text.grid(row=4, column=1, padx=20, pady=10)

# Run the application
root.mainloop()
