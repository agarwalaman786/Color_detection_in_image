import cv2
import numpy as np
image=cv2.imread('fordetection.jpg')
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower_red=np.array([178,179,3])
upper_red=np.array([255,255,255])
Detection_of_image=cv2.inRange(hsv,lower_red,upper_red)
cv2.imshow('Original Image',image)
cv2.imshow('Detected Image',Detection_of_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


