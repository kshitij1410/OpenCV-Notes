#resacling video implies modifying its height and width to
#to a particular height and width
import  cv2 as cv 

def changeRes(width,height):
    #this method only work from live video
    capture.set(3,width)
    capture.set(4,height)
    #or you can change brightness of the live stream
  

def rescaleFrame(frame , scale=0.75):
    #this method works for images ,videos ,live video

    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions =(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# img =cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat',img)
# resize_img=rescaleFrame(img)
# cv.imshow('ResizeImage',resize_img)



capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue , frame=capture.read()  #isTrue means check whether the frame is ready or not
    # if isTrue is false (the frame could not be read that means we are end of the video then we simply break it.)
    frame_resize = rescaleFrame(frame,scale=.2)

    if isTrue:
    #   cv.imshow('Video',frame)
      cv.imshow('VideoResize',frame_resize)

      if cv.waitKey(20) & 0xFF==ord('d'):  #if d is pressed then break out the loop and stop display the video
        break
    else:
        break


capture.release()  #release the capture pointer
cv.destroyAllWindows()    


