from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#E9A178")

        message = text1.get(1.0, END)
        decrypted_message = polyalphabetic_decrypt(message)

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#E9A178").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(text2.get("1.0", "end-1c"))

    Button(text="SAVE DECRYPTED FILE", height="2", width=50, bg="#E9A178", fg="white", bd=0, command=save_file).place(
        x=10, y=400)


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#820000")

        message = text1.get(1.0, END)
        encrypted_message = polyalphabetic_encrypt(message)

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#820000").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(text2.get("1.0", "end-1c"))

    Button(text="SAVE ENCRYPTED FILE", height="2", width=50, bg="#820000", fg="white", bd=0, command=save_file).place(
        x=10, y=400)


def polyalphabetic_decrypt(ciphertext):
    key = code.get()
    key_length = len(key)
    plaintext = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(
                    (ord(char) - ord('a') - (ord(key[i % key_length].lower()) - ord('a'))) % 26 + ord('a'))
            else:
                decrypted_char = chr(
                    (ord(char) - ord('A') - (ord(key[i % key_length].upper()) - ord('A'))) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


def polyalphabetic_encrypt(plaintext):
    key = code.get()
    key_length = len(key)
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(
                    (ord(char) - ord('a') + (ord(key[i % key_length].lower()) - ord('a'))) % 26 + ord('a'))
            else:
                encrypted_char = chr(
                    (ord(char) - ord('A') + (ord(key[i % key_length].upper()) - ord('A'))) % 26 + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x470")
    screen.title("CryptoCoder")

    def load_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as f:
                text1.delete("1.0", "end")
                text1.insert("1.0", f.read())

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Label(text="Created by: G35", fg="black", font=("calibri", 10)).place(x=10, y=445)

    Button(text="ENCRYPT", height="2", width=23, bg="#820000", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#E9A178", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#4E6C50", fg="white", bd=0, command=reset).place(x=10, y=300)
    Button(text="OPEN FILE", height="2", width=50, bg="#4E6C50", fg="white", bd=0, command=load_file).place(x=10, y=350)

    screen.mainloop()


main_screen()
