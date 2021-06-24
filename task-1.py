import cv2
import imutils
import matplotlib

img=cv2.imread('nature.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage", gray_img)
cv2.waitKey(0)

canny_low = cv2.Canny(gray_img,30,150)
cv2.imshow("low",canny_low)
cv2.waitKey(0)

canny_mid = cv2.Canny(gray_img, 50,170)
cv2.imshow("mid",canny_mid)
cv2.waitKey(0)

canny_high = cv2.Canny(gray_img,165,170)
cv2.imshow("high",canny_high)
cv2.imwrite("canny_high.jpg",canny_high)
cv2.waitKey(0) 
