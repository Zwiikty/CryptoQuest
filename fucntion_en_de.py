import os
from Crypto.Cipher import AES
from PIL import Image
from Crypto.Random import get_random_bytes
from tkinter import filedialog, ttk, END, messagebox
from gui import entry_1, entry_2, entry_3, entry_4, button_1, button_2, button_3, button_4

def openfile_encryption():
    file = filedialog.askopenfile(
        mode="r",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Csv Files", "*.csv"),
            ("Image Files", "*.png *.jpg *.jpeg *.jp2 *.tiff *.ppm *.bmp"),
            ("Music Files", "*.mp3 *.wav"),
            ("Video Files", "*.mp4 *.mov"),
        ],
    )
    if file:
        entry_2.delete(0, END)
        filepath = os.path.abspath(file.name)
        entry_2.insert(END, str(filepath))
        
def openfile_decryption():
    file = filedialog.askopenfile(
        mode="r",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Csv Files", "*.csv"),
            ("Image Files", "*.png *.jpg *.jpeg *.jp2 *.tiff *.ppm *.bmp"),
            ("Music Files", "*.mp3 *.wav"),
            ("Video Files", "*.mp4 *.mov"),
        ],
    )
    if file:
        entry_3.delete(0, END)
        filepath = os.path.abspath(file.name)
        entry_3.insert(END, str(filepath))

def filetype(plaintext):
    _, file_extension = os.path.splitext(plaintext)
    return file_extension

#encryption function
def encrypt_button_event():
    password = entry_4.get()
    if not password :
            messagebox.askretrycancel(";(", "Please enter your key")
            return
    
    password = entry_4.get()
    key_en = make_16_bytes(password)
    inputfile = entry_2.get()
    encrypted_file = "encrypted_file" + filetype(inputfile)
    encrypt_file(inputfile, encrypted_file, key_en)
    messagebox.showinfo("Success!!", "Encrypt file complete")
    entry_2.delete(0, END)
    entry_4.delete(0, END)

def encrypt_file(input_file, output_file, key):
        cipher = AES.new(key, AES.MODE_EAX)
        with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
            ciphertext, tag = cipher.encrypt_and_digest(infile.read())
            outfile.write(cipher.nonce)
            outfile.write(tag)
            outfile.write(ciphertext)

#decryption
def decrypt_button_event():     
    password = entry_1.get() 
    if not password :
        messagebox.askretrycancel("Warning", "Please don't forget the password")
        return
    password = entry_1.get()
    key_de = make_16_bytes(password)
    inputfile = entry_3.get()
    decrypted_file = "decrypted_file" + filetype(inputfile)
    decrypt_file(inputfile, decrypted_file, key_de)
    messagebox.showinfo("Success!!", "Decrypt file complete")
    entry_3.delete(0, END)
    entry_1.delete(0, END)
        
def filetype(plaintext):
    _, file_extension = os.path.splitext(plaintext)
    return file_extension

def make_16_bytes(text):
        byte_object = bytes(text, "utf-8")
        padding_length = 16 - len(byte_object)
        padding = b"\x01" * padding_length
        padded_byte_object = padding + byte_object
        return padded_byte_object

def decrypt_file(input_file, output_file, key):
        with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
            nonce = infile.read(16)
            tag = infile.read(16)
            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            ciphertext = infile.read()
            plaintext = cipher.decrypt(ciphertext)
            outfile.write(plaintext)

    