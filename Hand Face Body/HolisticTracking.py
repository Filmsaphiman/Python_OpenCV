import cv2
import  mediapipe as mp

cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\Ice Sketch.mp4")

mp_holistic = mp.solutions.holistic
"""
mpHand = mp.solutions.hands 
Hand = mpHand.Hands() 

mp_holistic = mp.solutions.holistic
with mp_holistic.Holistic() as  holistic:
"""
mp_drawing = mp.solutions.drawing_utils

with mp_holistic.Holistic() as holistic:
    while True:
        check , frame = cap.read()
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result = holistic.process(img)
        # print(result.face_landmarks)

        """
        .holistic -----> จะมี right_hand_landmarks , left_hand_landmarks , face_landmarks , pose_landmarks เป็นต้น
                  -----> จะไม่มี multi_hand_landmarks
          
        .Hands() , .hands() -----> จะมี multi_hand_landmarks , multi_hand_world_landmarks , multi_handedness เป็นต้น
        """
        # RGB to BGR
        frame = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        # face landmark
        mp_drawing.draw_landmarks(frame,result.face_landmarks,mp_holistic.FACEMESH_CONTOURS)
        # right hand landmark
        mp_drawing.draw_landmarks(frame, result.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        # left hand landmark
        mp_drawing.draw_landmarks(frame, result.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        # pose landmark
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv2.imshow("Output",frame)
        cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()


