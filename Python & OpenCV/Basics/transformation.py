import cv2 as cv
import numpy as np


img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # create translation matrix
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

  # -x --->left
  #  x--->right
  #  -y--->up
  #   y--->down


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        # assume we have to rotate around the center
        rotPoint = (width//2, height//2)
        # (rotPoitn , angle,scaling the image)
        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)  # clock wise -45 , #anticlockwise 45
cv.imshow("Rotated", rotated)


# Resizing image

  # resized1 = cv.resize(img, (500,500) ,interpolation = cv.INTER_AREA)
  # resized2 = cv.resize(img, (500,500) ,interpolation = cv.INTER_LINEAR)
resized3 = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
  # ENLARGING THE IMAGE - cv.INTER_LINEAR,cv.INTER_CUBIC
  # SHRINKING THE IMAGE - cv.INTER_AREA

  # cv.imshow("Resized1", resized1)
  # cv.imshow("Resized2", resized2)
cv.imshow("Resized3", resized3)


# Flipping
  #flipcode - 1,0,-1
  #   0-->flip vertically
  #   1-->flip horizontally
  #   -1-->flip both

flip = cv.flip(img, 0)
cv.imshow("Vertically flip", flip)


# Cropping

cropped = img[200:300, 300:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)


