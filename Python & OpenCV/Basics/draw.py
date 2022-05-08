import cv2 as cv
import numpy as np
#(rgb have 3 color dimension)
# ((height,wide,dimension) , data type - uusigned integer 8 bit


# ----------------blank image 
blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Image',blank)


#------------------------------------------------
#1.paint the image a certain color
    #format (blue,green , red)
blank[:] = 0,255,0 #rgb value - green color

   # blank[200:300, 300:400]=0,0,255    

cv.imshow('Green',blank)

# ----------------------------------------------------
#2.draw a rectangle
   # cv.rectangle((img),(x1,y1) ,(x2,y2) (intensity in blue,green,red),(line thickness))
   # line thickness -1 - solid
cv.rectangle((blank),(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,85),-1)
cv.imshow('Rectangle',blank)

#-----------------------------------------------------
# 3.Draw a circle
   # cv.circle((img),(center-x,center-y) (radius) ,(b,g,r),(thickness))

cv.circle((blank),(200,200),(100),(0,255,255),-1)
cv.imshow('Circle',blank)


#-------------------------------------------------------
#4.Draw a line
   #cv.line((img),(x1-corrdinate,y1),(x2,y2),(b,g,r),thickness in pixel)
cv.line(blank,(200,200),(300,320),(30,65,155),25)
cv.imshow('Line',blank) 


#------------------------------------------------------
#5.Write text on image
   # cv.putText(img,text,origin,fontface,fontscale,color,thickness)
cv.putText(blank,"Hi this is kshitij",(200,300),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),3)
cv.imshow('text',blank) 





cv.waitKey(0)
cv.destroyAllWindows()