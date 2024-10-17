import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detecter = HandDetector(detectionCon=0.8)

while True:
    check,frame = cap.read()
    hands , frame = detecter.findHands(frame)
    cv2.imshow("Output",frame)
    cv2.waitKey(1)