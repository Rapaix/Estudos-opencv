import numpy as np
import cv2

canvas = np.zeros((600, 600, 3), dtype="uint8")
green = (0,255,127)
branco = (255,255,255)
blue =(255, 0,0)
cv2.line(canvas,(300,150),(500,450),branco)
cv2.line(canvas,(300,150),(300,450),branco)
cv2.line(canvas,(300,150),(90,450),branco )
cv2.line(canvas,(90,450),(500,450),branco)
#cv2.line(canvas,(),(),red)
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)


#cv2.imshow("Canvas", canvas)
#v2.waitKey(0)