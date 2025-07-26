import cv2 as cv
import mediapipe as mp
import time
import numpy as np

cTime = 0
pTime = 0

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False, 3)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h) # Center of the landmark
                cv.circle(img, (cx, cy), 10, (255, 0, 255), cv.FILLED)
                print(id, cx, cy)
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)


    cv.imshow("Image", img)
    cv.waitKey(1)