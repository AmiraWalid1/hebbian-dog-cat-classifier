#!/usr/bin/python3
'''
This script is a specialized utility designed to streamline the process of image resizing.
It operates by sourcing images from a designated ‘data’ folder,
applies a resizing operation to each image,
and subsequently stores the resized images in a separate ‘data2’ folder.
'''
import cv2

dim = (300, 300)

for i in range(10):
    img1 = cv2.imread(f"./data/cat.{i}.jpg", cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread(f"./data/dog.{i}.jpg", cv2.COLOR_BGR2GRAY)

    resized1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
    resized2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(f"./data2/cat.{i}.jpg", resized1)
    cv2.imwrite(f"./data2/dog.{i}.jpg", resized2)
cv2.destroyAllWindows()
