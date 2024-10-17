"""
import cv2

img = cv2.imread("D:\Python\OpenCVimg\Image\coine.jpg")
img = cv2.resize(img,(500,370))

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# thresh , th = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)

# cv2.adaptiveThreshold จะใช้ได้ ก็ต่อเมื่อภาพถูกแปลงเป็น cv2.COLOR_BGR2GRAY แล้วเท่านั้น ไม่เช่นนั้นก็จะ error

cv2.imshow("Image",th)
cv2.waitKey(0)
"""
drinks = ['tea', 'coffee', 'cappuccino', 'lemonade']
enumerated_drinks = enumerate(drinks)
print(type(enumerated_drinks))
print(enumerated_drinks)
