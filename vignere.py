import tkinter as tk
from tkinter import messagebox


# Vigenère cipher functions
def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)


def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)


# GUI Functions
def encrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if not text or not key:
        messagebox.showerror("Error", "Please provide both text and key.")
        return
    encrypted = encrypt_vigenere(text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted)


def decrypt_message():
    text = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if not text or not key:
        messagebox.showerror("Error", "Please provide both text and key.")
        return
    decrypted = decrypt_vigenere(text, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted)


# GUI setup
root = tk.Tk()
root.title("Vigenère Cipher")

# Input text
tk.Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=10, pady=5)

# Key entry
tk.Label(root, text="Key:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Output text
tk.Label(root, text="Output Text:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=3, column=1, padx=10, pady=5)

# Run the application
root.mainloop()
