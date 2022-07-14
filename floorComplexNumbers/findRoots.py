# import the necessary packages
import numpy as np
import argparse
import cv2

brightnessThresh = 62

def adjustPoint(pixelValue: tuple, gray, scale: int):
	pixelWidth = pixelValue[0]
	pixelHeight = pixelValue[1]

	height = gray.shape[0]
	width = gray.shape[1]

	return complex(((pixelWidth - width/2)/width) * scale, ((pixelHeight - height/2)/height) * scale)

def kill_pixels(second, minLoc: tuple):
	second[minLoc[1] + 1][minLoc[0] + 1] = 255
	second[minLoc[1] + 1][minLoc[0]] = 255
	second[minLoc[1] - 1][minLoc[0] + 1] = 255
	second[minLoc[1]][minLoc[0] + 1] = 255
	second[minLoc[1]][minLoc[0] - 1] = 255
	second[minLoc[1] - 1][minLoc[0] - 1] = 255
	if second[minLoc[1]][minLoc[0]] <= brightnessThresh:
		return (kill_pixels(second, (minLoc[0] + 1, minLoc[1] + 1)), kill_pixels(second, (minLoc[0] + 1, minLoc[1])), kill_pixels(second, (minLoc[0], minLoc[1] + 1)), kill_pixels(second, (minLoc[0] - 1, minLoc[1] + 1)), kill_pixels(second, (minLoc[0] + 1, minLoc[1] - 1)), kill_pixels(second, (minLoc[0] - 1, minLoc[1] - 1)))

def checkIfValid(rootsList: list, root):
	for checkRoot in rootsList:
		distance = ((checkRoot[0] - root[0])**2 + (checkRoot[1] - root[1])**2 ) ** 0.5
		if distance < 20:
			return False
	return True

def getRoots(path: str, scale: int):
	roots = []
	pixelRoots = []
	# load the image and convert it to grayscale
	image = cv2.imread(path)
	orig = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# # perform a naive attempt to find the (x, y) coordinates of
	# # the area of the image with the largest intensity value
	# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
	# print(minLoc)

	# cv2.circle(image, minLoc, 5, (255, 0, 0), 2)
	# print(path.split(".png")[0] + ": " + str(adjustPoint(minLoc, gray)))

	minVal2 = 0
	cpy = gray.copy()
	prevLoc = (500, 500)
	while minVal2 < brightnessThresh:
		(minVal2, maxVal2, minLoc2, maxLoc2) = cv2.minMaxLoc(cpy)
		kill_pixels(cpy, minLoc2)
		if checkIfValid(pixelRoots, minLoc2):
			cv2.circle(image, minLoc2, 5, (255, 0, 0), 2)
			pixelRoots.append(minLoc2)
			adjustedRoot = adjustPoint(minLoc2, gray, scale)
			print(path.split(".png")[0] + ": " + str(adjustedRoot))
			roots.append(adjustedRoot)
	cv2.imshow("Complex Graphs", image)
	cv2.waitKey(1)
	return roots

def test():
	getRoots("./plotsRgb/z^2 + 0[z] + 1.0999999999999999.png")

if __name__ == "__main__":
	test()