import cv2
import mediapipe as mp
import winsound
import math
face_mesh = mp.solutions.face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
x1 = y1 = x2 = y2 = 0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    success , image = cap.read()
    if not success:
        break
    image = cv2.flip(image ,1)
    frame_height , frame_width , _ = image.shape
    rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_image)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmark = landmark_points[0].landmark
        for id , landmark in enumerate(landmark):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            
            if id == 13:
                x1 = x
                y1 = y
            if id == 14:
                x2 = x
                y2 = y
                # Dono corners par dots banao check karne ke liye
       
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5 //4
        if dist>1:
            cv2.imwrite("selfie.png", image)
            winsound.PlaySound("sound.wav",winsound.SND_FILENAME)
            
        
    cv2.imshow("Selfie taker AI",image)       
    key = cv2.waitKey(10)
            
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()