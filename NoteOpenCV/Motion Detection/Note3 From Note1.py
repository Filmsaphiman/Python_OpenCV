import cv2
cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\Ice Sketch.mp4")


while True:
    check , frame1 = cap.read()
    check , frame2 = cap.read()
    if check == True :
        diff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        erosion = cv2.erode(blur,(5,5),iterations = 3)
        thresh , result = cv2.threshold(erosion,50,255,cv2.THRESH_BINARY)
        cv2.imshow("Output",result)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyWindow()