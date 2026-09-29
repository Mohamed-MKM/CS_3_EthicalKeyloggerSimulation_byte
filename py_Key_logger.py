import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox


KEY_FILE = "encryption.key"
LOG_FILE = "keystrokes.enc"


def create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


def save_keystroke(key):
    encryption = Fernet(load_key())

    if key == "space":
        key = " "
    elif key == "Return":
        key = "[ENTER]"
    elif key == "BackSpace":
        key = "[BACKSPACE]"
    elif key == "Tab":
        key = "[TAB]"
    elif len(key) > 1:
        key = f"[{key}]"

    encrypted_data = encryption.encrypt(key.encode())

    with open(LOG_FILE, "ab") as file:
        file.write(encrypted_data + b"\n")


def handle_key(event):
    save_keystroke(event.keysym)


def purge_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        messagebox.showinfo("Purge", "Encrypted key log has been deleted.")
    else:
        messagebox.showinfo("Purge", "No key log was found.")


def start_program():
    create_key()

    window = tk.Tk()
    window.title("Ethical Keylogger Simulation")
    window.geometry("600x400")

    title = tk.Label(
        window,
        text="Ethical Keylogger Simulation",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=15)

    instructions = tk.Label(
        window,
        text="Type only test data in the box below.\n"
             "Keystrokes are captured only inside this window.",
        font=("Arial", 11)
    )
    instructions.pack(pady=10)

    text_box = tk.Text(
        window,
        height=10,
        width=60
    )
    text_box.pack(pady=10)

    purge_button = tk.Button(
        window,
        text="Purge Encrypted Log",
        command=purge_log
    )
    purge_button.pack(pady=10)

    text_box.bind("<KeyPress>", handle_key)

    window.mainloop()


if __name__ == "__main__":
    start_program()