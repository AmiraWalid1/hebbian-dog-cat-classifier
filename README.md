# Image Classifier using Hebbian Learning
This application, powered by Hebbian Learning, classifies images as cats 🐱 or dogs 🐶.

## Features

- **GUI**: The script uses Tkinter to create a graphical user interface (GUI) for the application. The GUI includes buttons for uploading images and initiating the Hebbian model, labels to display the uploaded image and the classification result, and a pie chart to display the accuracy of the model.
- **Hebbian Model**: The script uses a Hebbian learning model to classify the images. The model is trained on a set of images of cats and dogs.
- **Image Upload**: Users can upload an image using the 'upload' button. The image is then processed and classified as either a cat or a dog.
- **Accuracy Calculation**: The script calculates the accuracy of the model by comparing the model's predictions with the actual labels of a set of test images.


## Usage

To use the script, run it in a Python environment that has the necessary libraries installed (Tkinter, PIL, cv2, numpy, and matplotlib). The main window of the application will open, and you can start using the features of the application.

Please note that the script expects the training and test images to be located in specific directories (`data2` for training images and `test` for test images), and the images should be named in a specific format (`cat.{i}.jpg` and `dog.{i}.jpg` for training images, `{i}.jpg` for test images). Make sure these images are available and named correctly before running the script.

## Disclaimer

This script is a simple image classifier and is not intended to be used for complex image classification tasks. The accuracy of the model may vary depending on the quality and variety of the training and test images. Always use high-quality images for best results. 

## Dependencies

- Python 3
- Tkinter
- PIL (Pillow)
- OpenCV (cv2)
- NumPy
- Matplotlib