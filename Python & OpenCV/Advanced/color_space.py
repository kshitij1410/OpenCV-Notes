#RGB,HSV,lamb -all are color space
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Basics/Photos/cat.jpg')
cv.imshow('Cat',img)

#convert bgr to rgb , inverse of bgr is rbg 
plt.imshow(img)
plt.show()

#convert BGR TO GRAY SCALE
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR TO HSB
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


cv.waitKey(0)


#Note : you cannot convert gray scale image to hsv
