import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue , frame=capture.read()  #isTrue means check whether the frame is ready or not
    # if isTrue is false (the frame could not be read that means we are end of the video then we simply break it.)
    
    if isTrue:
      cv.imshow('Video',frame)

      if cv.waitKey(20) & 0xFF==ord('d'):  #if d is pressed then break out the loop and stop display the video
        break
    else:
        break
    
capture.release()  #release the capture pointer
cv.destroyAllWindows()    
