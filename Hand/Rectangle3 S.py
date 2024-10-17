import cv2
import mediapipe as mp
import  numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

mpHand = mp.solutions.hands
Hand = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    check, frame1 = cap.read()
    check, frame2 = cap.read()

    imgRGB = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    result = Hand.process(imgRGB)

    print(result.multi_hand_landmarks)
    A = result.multi_hand_landmarks

    if check == True:

        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        median = cv2.medianBlur(gray, 5)
        thresh, result = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)
        # median = cv2.medianBlur(gray, 5)
        dilation = cv2.dilate(result, None, iterations=1)
        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, (5, 5), iterations=5)
        Gaussian = cv2.GaussianBlur(closing, (5, 5), 0)
        # result_2 = cv2.adaptiveThreshold(closing,128,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
        contour, hierarchy = cv2.findContours(Gaussian, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for cnt in contour:
            x,y,w,h = cv2.boundingRect(cnt)
            # img = cv2.drawContours(frame1, cnt, 0, (0, 255, 255), 2)
            # img = cv2.drawContours(frame1, cnt, -1, (0, 255, 255), 2)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            # box = np.int0(box)
            cv2.drawContours(img,box,0,(0,255,255),2)
            cv2.imshow("Image",img)


    if A:
        for landmark in A:
            mpDraw.draw_landmarks(frame1, landmark, mpHand.HAND_CONNECTIONS)
            # Hand.HandLandmark

    cv2.imshow("Image", frame1)
    cv2.waitKey(1)


