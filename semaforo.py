import numpy as np
import argparse
import cv2
import mahotas
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", image)

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("laplace", lap)
cv2.waitKey(0)


def lap(image):
    lap = cv2.Laplacian(image, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv2.imshow("laplace", lap)


