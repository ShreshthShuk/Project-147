from tkinter import *

root = Tk()

root.title("Encryption with ASCII Code")
root.geometry("400x400")

root.configure(background = "pink")

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.3, anchor=CENTER)

Label_ASCII = Label(root, text="Name in ASCII in - ", bg="purple", fg="white")
Label_Encrypted = Label(root, text="Encrypted Name - ", bg="purple", fg="white")

def ASCIIConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        Label_ASCII["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        Encrypted = ascii - 1
        Label_Encrypted["text"] += str(chr(Encrypted))
        
btn = Button(root, text="Display the ASCII and Encrypted", command=ASCIIConverter, bg="blue", fg="black")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
Label_ASCII.place(relx=0.5, rely=0.5, anchor=CENTER)
Label_Encrypted.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()