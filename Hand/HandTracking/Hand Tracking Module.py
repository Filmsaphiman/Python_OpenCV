# เตรียมคำสั่ง Solution
# เตรียมข้อมูลเกี่ยวกับมือ
# เตรียมคำสั่งสำหรับการวาดมือ

# การเปิดกล้อง และ check frame แต่ละ frame
# การตรวจจับ และหาตำแหน่ง landmark ของมือ โดยการใช้ .process
# หลังจากหาตำแหน่งของ landmark แล้ว ---> ให้เก็บตำแหน่งของ landmark เอาไว้ โดยใช้ .multi_hand_landmark
# การวาดตำแหน่ง และ landmark ของมือลงบน frame [แต่เนื่องจากมีหลายตำแหน่ง และเป็นฉาก frame ต่อเนื่อง จึงใช้ for loop]
# connect landmark แต่ละตำแหน่งที่วาดลงไปในมือ

import cv2
import mediapipe as mp
import time

class handDetector():

    def __init__(self , mode=False , maxHands=2 , model_complexity = 1 , detectionCon=0.5 , trackingCon=0.5):
       self.mode = mode # value = object / ตัวแปร = object
       self.maxHands = maxHands
       self.model_complexity = model_complexity
       self.detectionCon = detectionCon
       self.trackingCon = trackingCon

       self.mpHand = mp.solutions.hands # ---> คำสั่งเกี่ยวกับมือ
       self.Hand = self.mpHand.Hands( self.mode,self.maxHands,self.model_complexity,
                                      self.detectionCon,self.trackingCon) # ---> ข้อมูลเกี่ยวกับมือ
       self.mpDraw = mp.solutions.drawing_utils # ---> คำสั่งการวาดมือ

    def findHands(self,frame,Draw = True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.Hand.process(imgRGB)  # ---> ค้นหาตำแหน่งของมือ และ landmark

        if self.result.multi_hand_landmarks:
            for landmark_ in self.result.multi_hand_landmarks:
                if Draw :
                    self.mpDraw.draw_landmarks(frame, landmark_, self.mpHand.HAND_CONNECTIONS)
        return frame

    def findPositions(self,frame,handNo=0,Draw = True):

        landmarkList =[]
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo] # ตรวจสอบว่าเป็นมือหมายเลขที่เท่าไหร่

            for id, lm in enumerate(myHand.landmark): # หา landmark ของ myHand
                # Naja = frame.shape
                # print(Naja)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                landmarkList.append([id,cx,cy])
                if Draw:
                    cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return landmarkList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
            check , frame = cap.read()
            frame = detector.findHands(frame)
            landmarkList = detector.findPositions(frame) # แสดง lanกmark ทั้งหมด แต่...
            if len(landmarkList) != 0:
                print(landmarkList[4]) # ... print แค่ id หมายเลข 4

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)

            cv2.imshow("Image", frame)
            cv2.waitKey(1)

# เมื่อเรียกใช้ จะเป็นเหมือน Code จำลอง เพื่อแสดง Module นี้สามารถทำได้
if __name__== "__main__":
    main()