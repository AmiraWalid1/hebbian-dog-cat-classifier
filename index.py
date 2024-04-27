#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import webbrowser

if __name__ == "__main__":
    window = Tk()
    window.configure(bg="#EEF8D9")
    window.geometry("700x500")
    window.title("Who am I 👀️")
    window.resizable(height = None , width= None)
    HebianLabel = Label(text = "Hebbian" , fg="black" , bg = "#B4D3AC",  width="800" , font="Arial 15 bold").pack(); 
    uploadLabel = Label(text="Upload your photo" , font="Inter 9" , fg="black" , bg ="#EEF8D9").pack(anchor="se" , side=BOTTOM , pady= 50 , padx = 20) 
    hebbianModeButton = Button(text="Hebbian model" , fg="black" , bg="#81B774" , width=15 , font = "10").pack(side=RIGHT , padx= 190 , pady= 90)
    
    window.mainloop()