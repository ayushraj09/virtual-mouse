import cv2 as cv
import mediapipe as mp
import time
import hand_tracking.hand_tracking_module as htm
cTime = 0
pTime = 0
cap = cv.VideoCapture(0)
detector = htm.HandDetector()
while True:
    success, img = cap.read()
    img = cv.flip(img, 1)

    img = detector.findHands(img)
    findPosition = detector.findPosition(img)
    if len(findPosition) != 0:
        print(findPosition[4])
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
    cv.imshow("Image", img)
    cv.waitKey(1)