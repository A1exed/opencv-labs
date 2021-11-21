import cv2

print(cv2.getBuildInformation())

img = cv2.imread("assets/taxi-1932107_640.jpg")

cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
