import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import hand_tracking_module as htm
import pynput
from screeninfo import get_monitors

monitor = get_monitors()[0]  # Gets primary monitor
wScr, hScr = monitor.width, monitor.height

wCam, hCam = 640, 480
sWidth, sHeight = 1710, 1107
frameR = 90
smoothening = 5
plocX, plocY = 0, 0 # Previous location
clocX, clocY = 0, 0 # Current location
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandDetector(maxHands=1)
pTime = 0

while True:
    #1 Get image and landmarks
    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    try:
        lmList, bbox = detector.findPosition(img, draw=False)
        cv.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2)
        # 2. Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            # 3. Check which fingers are up
            fingers = detector.fingersUp()
            #print(fingers)

        # 4. Only Index Finger : Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move Mouse
            mouse = pynput.mouse.Controller()
            mouse.position = (clocX, clocY)
            cv.circle(img, (x1, y1), 15, (255, 0, 255), cv.FILLED)
            plocX, plocY = clocX, clocY

        # 8. Both Index and middle fingers are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)

            # 10. Click mouse if distance short
            if length < 40:
                cv.circle(img, (lineInfo[4], lineInfo[5]),
                15, (0, 255, 0), cv.FILLED)
                mouse.click(pynput.mouse.Button.left, 1)
            elif length >110:
                cv.circle(img, (lineInfo[4], lineInfo[5]),
                15, (0, 255, 0), cv.FILLED)
                mouse.click(pynput.mouse.Button.right, 1)
    except ValueError:
        # Handle case when no hand is detected
        lmList = []
        bbox = None

    # 11. Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (20, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0,
    0), 3)

    cv.imshow("Image", img)
    cv.waitKey(1)