import  cv2
import  numpy as np

Img = cv2.imread("D:\Python\OpenCVimg\Image\Thunder2.jpg")
#img = cv2.resize(Img,(250,400))
img = cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)

thresh , result = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
contours , hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
result = cv2.drawContours(Img, contours, -1, (255, 0, 255), 5)


#for (x,y,w,h ) in contours:
   #x,y,w,h = cv2.boundingRect(contour)
   #result = cv2.drawContours(img,contour,-1,(0,0,255),10)
   #result= cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),2)

cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
Img = cv2.rectangle(result,(x,y),(x+w,y+h),(255,0,255),2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
Img = cv2.drawContours(Img,[box], 0, (0, 0, 255), 2)



cv2.imshow("Output",Img)
cv2.waitKey()