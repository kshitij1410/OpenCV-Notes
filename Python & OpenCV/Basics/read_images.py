import cv2 as cv

# img = cv.imread('Photos/cat.jpg') #return matrix of pixel

# cv.imshow('Cat',img)  #(windowname,matrix)

# cv.waitKey(0) #keyboard binding function


#large img resoultion 
img1 = cv.imread('Photos/cat_large.jpg') 

# dimension of image is larger than the monitor dimension 
#it will be resolve by resizing and rescaling

cv.imshow('Cat1',img1)  

cv.waitKey(0) 