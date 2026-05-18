import cv2
from ultralytics import YOLO
import pygame
import time

model = YOLO('yolov8x-pose.pt') # model seçimi yolov8n hafif, m orta ,x yüksek

pygame.mixer.init()
pygame.mixer.music.load('ses.mp3')

cap = cv2.VideoCapture(0)
face_closed_start_time = None
play_sound= False

while cap.isOpened(): # eğer kamera açıksa True döner
    success, frame = cap.read() # başarılı olarak not geçer
    if not success: break # eğer başarılı dönmüyorsa direk programı kapatır

    # YOLOv8 ile görseli işle
    results = model(frame, verbose=False) # sonuçlar model içinde kare diyor ama IDK

    face_closed = False # başta yüz kapalıyı False olarak alıyor

    for r in results:
        if r.keypoints is not None and len(r.keypoints.conf) > 0:
            # keypoints.conf -> Bize noktaların güven skorunu verir (NumPy Array) ( senin yorum satırın sayesinde bunu anladım thx)
            # [0] ilk algılanan insan
            if len(r.keypoints.conf[0]):
                confidences = r.keypoints.conf[0].cpu().numpy()

            # güven skorunu alıyoruz
                person = confidences[0]


                if person < 0.4:
                 face_closed = True
            else:
                face_closed = True
        else:
            face_closed = False


    if face_closed:
        if face_closed_start_time is None:
            face_closed_start_time = time.time()

        if time.time() - face_closed_start_time > 0.5:
            if not play_sound:
                pygame.mixer.music.play(-1)
                play_sound = True
    else: # kapalı göz false dönerse zamanı başlatmıyor ve direk değersiz dönüyor
        face_closed_start_time = None
        pygame.mixer.music.stop()
        play_sound = False

    if None:
        cv2.imshow('YOLOv8 Pose')
    else:
        annotated_frame = results[0].plot()
        cv2.imshow('Yorgunsun Degilmi', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # çıkış için tuşu bekliyor
        break

cap.release()
cv2.destroyAllWindows()