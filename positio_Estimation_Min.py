import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPos =mp.solutions.pose
pose = mpPos.Pose()

cap = cv2.VideoCapture('videos/13.mova')
pTime=0
while True:
 success, img = cap.read()
 imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 results = pose.process(imgRGB)
 # print(results.pose_landmarks)
 if results.pose_landmarks:
  mpDraw.draw_landmarks(img, results.pose_landmarks,mpPos.POSE_CONNECTIONS)
  for id, lm in enumerate(results.pose_landmarks.landmark):
   h, w, c = img.shape
   print(id, lm)
   cx,cy= int(lm.x*w), int(lm.y*h)
   cv2.circle(img, (cx,cy),6,(255,0,0), cv2.FILLED)



 cTime = time.time()
 fps = 1/(cTime-pTime)
 pTime = cTime

 cv2.putText(img,str(int(fps)),(70,90),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
 cv2.imshow('Image', img)

 cv2.waitKey(1)
