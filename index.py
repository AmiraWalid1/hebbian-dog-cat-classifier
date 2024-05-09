#!/usr/bin/python3
# Import necessary modules
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, UnidentifiedImageError
import cv2
import numpy as np
import matplotlib.pyplot as plt


lbl = None
allInputs = []
T = []
weights = np.array([])
text = "Type is : ???"
text2 = "Accuracy is : ???"

# Define the function to upload and process an image
def open_image():
    global lbl, text
    try:
        # Open a file dialog and get the selected image path
        img_path = askopenfilename()
        # Open the image file
        img = Image.open(img_path)
        img_width, img_height = img.size

        # Resize the image so that its width and height are no more than 100 pixels.
        while img_width > 150 and img_height > 150:
            img_width *= .99
            img_height *= .99

        # Resize the image
        img = img.resize((int(img_width), int(img_height)))
        # Convert the image to a format that Tkinter can use
        img_tk = ImageTk.PhotoImage(img)
         
        if lbl :
            lbl.destroy()
        # Create a label with the image and pack it into the window
        lbl = Label(frame2, image=img_tk)
        lbl.image = img_tk  # Keep a reference to the image to prevent it from being garbage collected
        lbl.pack(pady=10)

        # Call the neural function
        neural(img_path)
    except UnidentifiedImageError:
        messagebox.showinfo(title='Upload Error',
                            message='Image could not be read, Please sure the selected is an image file.')

def orthonormal(pp):
    for i in range(len(pp)):
        for j in range(len(pp[0])):
            if (i==j and pp[i][j] != 1) or (i != j and pp[i][j]!=0):
                return False
            
    return True

def training():
    global weights, T, allInputs
    S = 1
    for i in range(10):
        allInputs.append(flatten(cv2.imread(f"data2/cat.{i}.jpg",cv2.IMREAD_GRAYSCALE)) )
        T.append([1 for _ in range(S)])
        allInputs.append(flatten(cv2.imread(f"data2/dog.{i}.jpg",cv2.IMREAD_GRAYSCALE)) )
        T.append([-1 for _ in range(S)])

    allInputs = np.array(allInputs)
    T = np.array(T).transpose()
    
    numP =  len(allInputs)
    R = len(allInputs[0])
    
    if orthonormal(allInputs):
        weights = np.dot(T, allInputs)
    else:
        weights = np.dot(T, np.dot(np.linalg.inv(np.dot(allInputs, allInputs.transpose())),allInputs))
    accuracy()
    Draw()

def Draw():
    cat_image_paths = [f"data2/cat.{i}.jpg" for i in range(10)]
    dog_image_paths = [f"data2/dog.{i}.jpg" for i in range(10)]
    cat_images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in cat_image_paths]
    dog_images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in dog_image_paths]

# Create a 2x5 grid for displaying images
    plt.figure(figsize=(10, 4))
    for i in range(10):
       plt.subplot(2, 5, i + 1)
       if i < 5:
          plt.imshow(cat_images[i], cmap='gray')
          plt.title(f"Cat {i}")
       else:
          plt.imshow(dog_images[i - 5], cmap='gray')
          plt.title(f"Dog {i - 5}")
    plt.axis('off')

    plt.suptitle("Training Images: Cats and Dogs")
    plt.tight_layout()
    plt.show()
    
    
def flatten(image):
    new_image = []
    for row in image:
        for el in row:
            new_image.append(-1 if el<128 else 1)
    return new_image

def neural(path):
    global weights, text
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (300, 300), interpolation = cv2.INTER_AREA)
    p = np.array(flatten(resized) )
    p = p.transpose()
    a = np.dot(weights, p)
    text = "Type is : Cat" if a[0] >= 0 else "Type is : Dog"
    
    lbl2.config(text=text)
    lbl2.text = text

def accuracy():
    p = []
    counter = 0
    for i in range(1,7):
        img = cv2.imread(f"test/{i}.jpg",cv2.IMREAD_GRAYSCALE)
        resized = cv2.resize(img, (300, 300), interpolation = cv2.INTER_AREA)
        p = np.array(flatten(resized) )
        p = p.transpose()
        a = np.dot(weights, p)
        counter += 1 if (a[0] >= 0 and i <= 3) or (a[0] < 0 and i > 3) else 0

    text2 = f"Accuracy is :{(counter/6.0)*100}%"
    lbl3.config(text=text2)
    lbl3.text = text2

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
    frame1 = Frame(window,width=400, height=499, bg="#EEF8D9")
    frame2 = Frame(window,width=400, height=200, bg="#EEF8D9")

    # Pack the frames to divide the window
    frame1.place(relx=0, y=30)
    frame2.place(relx=0.5, rely=0.2)

    # Create a label and pack it into the window
    HebianLabel = Label(window, text="Hebbian", fg="black", bg="#B4D3AC",  width="800", height="1", font="Arial 15 bold").pack()
    # Create a Hebbian model button and pack it into the frame1
    hebbianModeButton = Button(frame2, text="Hebbian model", fg="black", bg="#81B774", width=15, font="10", command=lambda: training()).pack()
    
    # Create a label for the accuracy
    lbl3 = Label(frame2, text=text2)
    lbl3.pack(pady=30)

    # Create upload label
    UploadLabel = Label(frame2, text="Upload your photo", fg="black", bg="#EEF8D9", width=15, height="1", font="Arial 10").pack()

    # Create an upload button and pack it into the frame1
    btn = Button(frame2, text='upload', fg="black", bg="#81B774", width=12, font="10", command=lambda: open_image()).pack()

    # Open, resize, and display a Dog image
    imgDog = Image.open('./photos/Dog.jpeg')
    resize_image_Dog = imgDog.resize((200, 200))
    imgD = ImageTk.PhotoImage(resize_image_Dog)
    lblCat = Label(frame1, image=imgD).pack(pady=20, padx=30)

    # Open, resize, and display a cat image
    imgCat = Image.open('./photos/Cat.jpeg')
    resize_image_cat = imgCat.resize((200, 200))
    imgC = ImageTk.PhotoImage(resize_image_cat)
    lblCat = Label(frame1, image=imgC).pack(pady=0, padx=30)

    # Create a label for the result
    lbl2 = Label(frame2, text=text)
    lbl2.pack()

    # Start the main event loop
    window.mainloop()