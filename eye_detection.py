#eye_detection_without_camera
import cv2

eye_cascade = cv2.CascadeClassifier(r"C:\Users\91630\Downloads\haarcascade_frontalface_default.xml")
pic = cv2.imread(r"C:\Users\91630\Downloads\WhatsApp Image 2023-03-01 at 2.12.45 PM.jpeg",0)

def detect_eyes(img):
    face_img = img.copy()
    eyes = eye_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5) 
    
    for (x,y,w,h) in eyes: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
    return face_img

result = detect_eyes(pic)

while True:
    cv2.imshow('',result)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
