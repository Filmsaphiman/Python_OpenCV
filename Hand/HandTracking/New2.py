import cv2
import mediapipe as mp
import time

class handDetector():
# __init__ นะ บ่แม่น __int__
    def __init__(self , mode=False , maxHands=2 , model_complexity = 1 , detectionCon=0.5 , trackingCon=0.5):
       self.mode = mode
       self.maxHands = maxHands
       self.model_complexity = model_complexity
       self.detectionCon = detectionCon
       self.trackingCon = trackingCon

       self.mpHands = mp.solutions.hands
       self.Hands = self.mpHands.Hands(self.mode,self.maxHands,self.model_complexity,
                                      self.detectionCon,self.trackingCon)
       self.mpDraw = mp.solutions.drawing_utils

    """
    def __init__(self, mode=False, maxHands=2, model_complexity=1, detectionCon=0.5, trackingCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpHands = mp.solutions.hands
        self.Hand = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity,
                                        self.detectionCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils
   """

    def findHands(self,frame,Draw = True):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.Hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for landmark_ in self.result.multi_hand_landmarks:
                if Draw :
                    self.mpDraw.draw_landmarks(frame, landmark_, self.mpHands.HAND_CONNECTIONS)
        return frame
"""
        def findHands(self, frame, Draw=True):
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.result = self.Hand.process(imgRGB)

            if self.result.multi_hand_landmarks:
                for landmark_ in self.result.multi_hand_landmarks:
                    if Draw:
                        self.mpDraw.draw_landmarks(frame, landmark_,
                                                   self.mpHands.HAND_CONNECTIONS)
            return frame
"""



            # for id, lm in enumerate(landmark_.landmark):
                #    # Naja = frame.shape
                #   # print(Naja)
                #    h, w, c = frame.shape
                #    cx, cy = int(lm.x * w), int(lm.y * h)
                #    print(id, cx, cy)
                #    if id == 0:
                #        cv2.circle(frame, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
            check , frame = cap.read()
            frame = detector.findHands(frame)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)

            cv2.imshow("Image", frame)
            cv2.waitKey(1)
if __name__== "__main__":
    main()