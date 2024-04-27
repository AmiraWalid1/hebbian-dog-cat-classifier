#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import webbrowser

if __name__ == "__main__":
    window = Tk()
    window.configure(bg="#EEF8D9")
    window.geometry("800x500")
    window.title("Who am I 👀️")
    window.resizable(height = None , width= None)
    window.resizable(0,0)
    

    HebianLabel = Label( window , text = "Hebbian" , fg="black" , bg = "#B4D3AC",  width="800" , font="Arial 15 bold").pack()
    hebbianModeButton = Button(window ,text="Hebbian model" , fg="black" , bg="#81B774" , width=15 , font = "10").pack(side=RIGHT , padx= 190 , pady= 90)
    uploadLabel = Label(text="Upload your photo" , font="Inter 9" , fg="black" , bg ="#EEF8D9") .pack(anchor="n") 
   

    imgCat = Image.open('C:/Users/SOUQ COMPUTER/Downloads/cat1.png')
    resize_image_cat = imgCat.resize((200 , 200))
    imgC = ImageTk.PhotoImage(resize_image_cat)
    lblCat = Label(image= imgC).pack(pady=20)
    
    imgDog = Image.open('C:/Users/SOUQ COMPUTER/Downloads/dog1.png')
    resize_image_Dog = imgDog.resize((200 , 200))
    imgD = ImageTk.PhotoImage(resize_image_Dog)
    lblCat = Label(image= imgD).pack(pady=10)

    window.mainloop()