import  cv2
cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\BP.mp4")

while True:
    check , frame = cap.read()
    if check == True:

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        theesh , result = cv2.threshold(blur,128,255,cv2.THRESH_BINARY)
        contour , hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame,contour,-1,(0,255,0),2)
        gray = frame
        cv2.imshow("Output",gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cv2.release()
cv2.destroyAllWindows()