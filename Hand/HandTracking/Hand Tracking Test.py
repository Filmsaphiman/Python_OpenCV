import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands # hands --> เตรียมคำสั่งตรวจจับมือ
Hand = mpHand.Hands() # Hands --> เตรียมข้อมูลมือจาก mpHand แล้วเก็บไว้ใน Hand
mpDraw = mp.solutions.drawing_utils # mp.solutions.drawing_utils = การวาดผลลัพธ์ลงไป

# hands = คำสั่งตรวจจับมือ
# Hands = ข้อมูลมือ
# MediaPipe Hands ประมวลผลภาพ RGB และส่งคืน Hand Landmarks
# ความถนัด (มือซ้ายเทียบกับมือขวา) ของมือแต่ละมือที่ตรวจพบ

while True:
    check , frame = cap.read()
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = Hand.process(imgRGB)

    print(result.multi_hand_landmarks)
    A = result.multi_hand_landmarks

    if A:
        for landmark in A:
            mpDraw.draw_landmarks(frame,landmark,mpHand.HAND_CONNECTIONS)
            # mpDraw.draw_landmarks --> นำ LandMark มาวาดเป็นผลลัพธ์

    cv2.imshow("Image",frame)
    cv2.waitKey(1)


