import tkinter as tk
from PIL import Image
from tkinter import messagebox
from functools import partial  


def decode(e3):
    image=e3.get()
    img=Image.open(image,'r')

    width, height = img.size
    msg = ""
    index = 0

    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1

    tk.messagebox.showinfo("Encoded Message", msg)

    
def encode(e1,e2):
    image=e1.get()
    img=Image.open(image,'r')

    msg=e2.get()
    length = len(msg)

    encoded = img.copy()

    width, height = img.size
    index = 0

    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1

    encoded.save("/Users/nachiketh/Desktop/encoded_image.png")

    tk.messagebox.showinfo("Encoding", "Encryption successfull")


def Decrypt():
    decrypt = tk.Tk()
    decrypt.geometry('400x200+100+200')
    decrypt.title('Decryption')

    img_location = tk.StringVar()   

    tk.Label(decrypt, text="Image location").grid(row=0, column=0)  

    e3 = tk.Entry(decrypt,textvariable=img_location)

    e3.grid(row=0, column=50)

    tk.Button(decrypt, text='Decrypt', command=partial(decode,e3)).grid(row=3, column=1, sticky=tk.W, pady=4)

    
def Encrypt():
    encrypt = tk.Tk()
    encrypt.geometry('400x200+100+200')  
    encrypt.title('Encryption')

    img_location = tk.StringVar()  
    encryption_text = tk.StringVar()  

    tk.Label(encrypt, text="Image location").grid(row=0, column=0)    
    tk.Label(encrypt, text="Text to be encrypyted").grid(row=1, column=0)

    e1 = tk.Entry(encrypt,textvariable=img_location)
    e2 = tk.Entry(encrypt,textvariable=encryption_text)

    e1.grid(row=0, column=50)
    e2.grid(row=1, column=50)

    tk.Button(encrypt, text='Encrypt', command=partial(encode,e1,e2)).grid(row=3, column=1, sticky=tk.W, pady=4)
    tk.Button(encrypt, text='Quit', command=master.quit).grid(row=4, column=1, sticky=tk.W, pady=4)


master = tk.Tk()
master.geometry('400x200+100+200')  
master.title('Steganography')
tk.Button(master, text='Encrypt', command=Encrypt).grid(row=2, column=2, sticky=tk.W, pady=4)
tk.Button(master, text='Decrypt', command=Decrypt,).grid(row=3, column=2, sticky=tk.W, pady=4)

tk.mainloop()