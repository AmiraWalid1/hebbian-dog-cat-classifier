#!/usr/bin/python3
# Import necessary modules
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, UnidentifiedImageError
import webbrowser


# Define the function to upload and process an image
def upload_action():
    try:
        # Open a file dialog and get the selected image path
        img_path = askopenfilename()
        # Open the image file
        img = Image.open(img_path)
        img_width, img_height = img.size

        # Resize the image so that its width and height are no more than 100 pixels.
        while img_width > 100 and img_height > 100:
            img_width *= .99
            img_height *= .99

        # Resize the image
        img = img.resize((int(img_width), int(img_height)))
        # Convert the image to a format that Tkinter can use
        img_tk = ImageTk.PhotoImage(img)

        # Create a label with the image and pack it into the window
        lbl = Label(frame1, image=img_tk)
        lbl.image = img_tk  # Keep a reference to the image to prevent it from being garbage collected
        lbl.pack()
    except UnidentifiedImageError:
        messagebox.showinfo(title='Upload Error',
                            message='Image could not be read, Please sure the selected is an image file.')


# Main program
if __name__ == "__main__":
    # Create the main window
    window = Tk()
    # Configure the window
    window.configure(bg="#EEF8D9")
    window.geometry("800x500")
    window.title("Who am I 👀️")
    window.resizable(height=None, width=None)
    window.resizable(0, 0)

    # Create two frames
    frame1 = Frame(window, bg="#EEF8D9")
    frame2 = Frame(window, bg="#EEF8D9")

    # Pack the frames to divide the window
    frame1.pack(side=RIGHT)
    frame2.pack(side=LEFT)

    # Create a label and pack it into the window
    HebianLabel = Label(window, text="Hebbian", fg="black", bg="#B4D3AC",  width="800", height="1", font="Arial 15 bold").pack(fill=X)
    # Create a Hebbian model button and pack it into the frame1
    hebbianModeButton = Button(frame1, text="Hebbian model", fg="black", bg="#81B774", width=15, font="10").pack(padx=120)

    # Create an upload button and pack it into the frame1
    btn = Button(frame1, text='upload', fg="black", bg="#81B774", width=10, font="10", command=lambda: upload_action()).pack(padx=100)

    # Open, resize, and display a Dog image
    imgDog = Image.open('./photos/Dog.jpeg')
    resize_image_Dog = imgDog.resize((200, 200))
    imgD = ImageTk.PhotoImage(resize_image_Dog)
    lblCat = Label(frame2, image=imgD).pack(pady=20, padx=30)

    # Open, resize, and display a cat image
    imgCat = Image.open('./photos/Cat.jpeg')
    resize_image_cat = imgCat.resize((200, 200))
    imgC = ImageTk.PhotoImage(resize_image_cat)
    lblCat = Label(frame2, image=imgC).pack(pady=1, padx=30)

    # Start the main event loop
    window.mainloop()
