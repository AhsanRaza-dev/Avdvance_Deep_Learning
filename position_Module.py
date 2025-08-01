import cv2
import mediapipe as mp
import time

class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.uPBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPos = mp.solutions.pose
        self.pose = self.mpPos.Pose(self.mode, self.uPBody,
                                    self.smooth, self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
         self.results = self.pose.process(imgRGB)
         if self.results.pose_landmarks:
             if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPos.POSE_CONNECTIONS)
         return img

    def getPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
           for id, lm in enumerate(self.results.pose_landmarks.landmark):
               h, w, c = img.shape
               print(id, lm)
               cx,cy= int(lm.x*w), int(lm.y*h)
               lmList.append([id, cx, cy])
               if draw:
                   cv2.circle(img, (cx,cy),6,(255,0,0), cv2.FILLED)






def main():
    cap = cv2.VideoCapture('videos/12.mp4')
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.getPosition(img)
        print(lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 90),
                    cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        cv2.imshow('Image', img)

        cv2.waitKey(1)


if __name__ == "__main":
    main()