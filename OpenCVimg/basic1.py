import cv2
img = cv2.imread("image/L 6.jpg")
cv2.imshow("L",img)
print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()

