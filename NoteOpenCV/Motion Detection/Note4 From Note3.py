import cv2
cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\Ice Sketch.mp4")


while True:
    check , frame1 = cap.read()
    check , frame2 = cap.read()
    if check == True :
        diff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        #  thresh , result มาก่อน erosion
        thresh , result = cv2.threshold(blur,50,255,cv2.THRESH_BINARY)
        erosion = cv2.erode(result, (5, 5), iterations=3)
        contours , hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame1,contours,-1,(0,255,0),2)
        erosion = frame1
        cv2.imshow("Output",frame1)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cv2.release()
cv2.destroyWindow()