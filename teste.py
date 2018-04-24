import cv2
import numpy as np

img = cv2.imread('saitama.jpg', 0)
cv2.imshow("One", img)
k = cv2.waitkey(0) & 0xff
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('imagegray.png', img)
    cv2.destroyAllWindows()
