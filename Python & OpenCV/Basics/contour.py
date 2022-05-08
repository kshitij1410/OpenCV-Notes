import cv2 as cv
import numpy as np

# Read in an image
img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#blank image 
blank =np.zeros(img.shape,dtype="uint8")
cv.imshow("Blank",blank)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Edge Cascade
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny Edges', canny)

#thersholding attempts to binarize an image 
#it take an image and convert it into bianry form.
#i.e black or white
ret,thresh =cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)



# contours it is a list which store the coordinate\s of the edges
# hierachial store the hiearchial manner
contours, hierarchies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{ len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255) ,2)
cv.imshow('Contours Draw',blank)

cv.waitKey(0)
cv.destroyAllWindows()
