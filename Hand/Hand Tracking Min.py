# เตรียมคำสั่ง Solution
# เตรียมข้อมูลเกี่ยวกับมือ
# เตรียมคำสั่งสำหรับการวาดมือ

# การเปิดกล้อง และ check frame แต่ละ frame
# การตรวจจับ และหาตำแหน่ง landmark ของมือ โดยการใช้ .process
# หลังจากหาตำแหน่งของ landmark แล้ว ---> ให้เก็บตำแหน่งของ landmark เอาไว้ โดยใช้ .multi_hand_landmark
# การวาดตำแหน่ง และ landmark ของมือลงบน frame [แต่เนื่องจากมีหลายตำแหน่ง และเป็นฉาก frame ต่อเนื่อง จึงใช้ for loop]
# connect landmark แต่ละตำแหน่งที่วาดลงไปในมือ

"""
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:   [# Hand landmark 1 จุด (ใช้ตัวแปรเป็น handLms) ใน Hand landmark ทั้งหมด] 
            for id, lm in enumerate(handLms.landmark): [# หา id, lm ใน landmark 1 จุด นั้น]
                # print(id, lm)
                h, w, c = img.shape
                ...
                [คำว่า shape ใน NumPy หมายถึงการให้ข้อมูลว่า array นั้นมีสมาชิกกี่ตัว กี่แถว กี่คอลัมน์ และกี่ตาราง ]
                [x = np.array(1)                                                          ]
                [print(x.shape)                                                           ]
                [print(x)                                                                 ]
                [                                                                         ]
                [output:                                                                  ]
                [()                                                                       ]
                [1                                                                        ]
                ...
                [y = np.array([1,2,3])                                                    ]
                [print(y.shape)                                                           ]
                [print(y)                                                                 ]
                [                                                                         ]
                [output:                                                                  ]
                [(3,)                                                                     ]
                [[1 2 3]]                                                                 ]
                ...

                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands # ---> คำสั่งเกี่ยวกับมือ
Hand = mpHand.Hands() # ---> ข้อมูลเกี่ยวกับมือ
mpDraw = mp.solutions.drawing_utils # ---> คำสั่งการวาดมือ

pTime = 0
cTime = 0

while True:
    check , frame = cap.read()
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = Hand.process(imgRGB) # ---> ค้นหาตำแหน่งของมือ และ landmark
    A = result.multi_hand_landmarks
    #print(A)

    if A:
        for landmark_ in A:
            for id, lm in enumerate(landmark_.landmark):
                #Naja = frame.shape  [โดยที่ frame.shape ส่งกลับ (ความสูง , ความกว้าง , จำนวนช่องสัญญาณ)]
                #print(Naja) -----> Output is 480(ความสูง) , 640(ความกว้าง) ,3(ำนวนช่องสัญญาณ)
                h, w, c = frame.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                print(id,cx,cy)
                if id == 0:
                    cv2.circle(frame,(cx,cy),15,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(frame,landmark_,mpHand.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,5,(255,0,255),3)

    cv2.imshow("Image",frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()