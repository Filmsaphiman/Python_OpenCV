import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cv2.CAP_DSHOW ทำหน้าที่อะไรไม่รู้ รุ้แต่ว่า ใช้แล้วทำให้ frame สมูทขึ้นมาก(frame ไม่สะดุด)

while True :
    check , frame1 = cap.read()
    check , frame2 = cap.read()
    if check == True :
        diff = cv2.absdiff(frame1,frame2)
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        median = cv2.medianBlur(gray,5)
        thresh , result = cv2.threshold(gray,15,255,cv2.THRESH_BINARY)
        #median = cv2.medianBlur(gray, 5)
        dilation = cv2.dilate(result,None,iterations=1)
        closing = cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,(5,5),iterations=5)
        Gaussian = cv2.GaussianBlur(closing,(5,5),0)
        # result_2 = cv2.adaptiveThreshold(closing,128,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)

        cv2.imshow("Image", Gaussian)
        cv2.waitKey(1)
