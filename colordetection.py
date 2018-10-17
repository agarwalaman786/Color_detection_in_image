import cv2
import numpy
image=cv2.imread('color.jpg')
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
x=raw_input("Enter the color you want to detect\n")
if x=='blue' or x=='Blue' or x== 'BLUE':
   lower_blue = numpy.array([110,50,0])
   upper_blue = numpy.array([130,255,255])
   Detection_of_image=cv2.inRange(hsv,lower_blue,upper_blue)
   cv2.imshow('Original Image',image)
   cv2.imshow('Detected Image',Detection_of_image)
elif x=='red' or x=='RED' or x=='Red':
   lower_red = numpy.array([179,179,0])
   upper_red = numpy.array([255,255,255])
   Detection_of_image=cv2.inRange(hsv,lower_red,upper_red)
   cv2.imshow('Original Image',image)
   cv2.imshow('Detected Image',Detection_of_image)
elif x=='green' or x=='GREEN' or x=='Green':
   lower_green = numpy.array([65,60,0])
   upper_green = numpy.array([80,255,255])
   Detection_of_image=cv2.inRange(hsv,lower_green,upper_green)
   cv2.imshow('Original Image',image)
   cv2.imshow('Detected Image',Detection_of_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

