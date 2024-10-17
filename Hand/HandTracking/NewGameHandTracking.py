import cv2
import mediapipe as mp
import time
from cvzone.HandTrackingModule import HandDetector


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    check, frame = cap.read()
    frame = detector.findHands(frame, draw=True ) # ให้ใช้ keyword เป็น 'draw' ไม่ใช่ Draw
    landmarkList = detector.findPosition(frame, draw=False) # ให้ใช้ keyword เป็น 'draw' ไม่ใช่ Draw
    if len(landmarkList) != 0:
        print(landmarkList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
    #           (255, 0, 255), 3)

    cv2.imshow("Image", frame)
    cv2.waitKey(1)