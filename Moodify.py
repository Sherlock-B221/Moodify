from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
import webbrowser as wb

detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'

face_detection = cv2.CascadeClassifier(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
 "neutral"]

cv2.namedWindow('your_face')
camera = cv2.VideoCapture(0)
i = 0
for q in range(10):
    frame = camera.read()[1]
    frame = imutils.resize(frame,width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    
    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()

    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
        key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
       
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]
        print(label)
        a = label
    else: continue

 
    for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                text = "{}: {:.2f}%".format(emotion, prob * 100)
                w = int(prob * 300)
                cv2.rectangle(canvas, (7, (i * 35) + 5),
                (w, (i * 35) + 35), (0, 0, 255), -1)
                cv2.putText(canvas, text, (10, (i * 35) + 23),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                (255, 255, 255), 2)
                cv2.putText(frameClone, label, (fX, fY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                              (0, 0, 255), 2)


    cv2.imshow('your_face', frameClone)
    cv2.imshow("Probabilities", canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Final Emotion is {}".format(a))
        if a == "happy":
            wb.open("https://www.youtube.com/watch?v=6-OvO8ZuW98&list=PLinS5uF49IBo8HLKBDAjQaeiN4TjHi75Q&index=3")
        elif a == "neutral":
            wb.open("https://www.youtube.com/watch?v=Pkh8UtuejGw&list=PLj_TM1PlrIA3aFxJH7NGhx7UM1OCuTYT9&index=2")
        elif a == "sad":
            wb.open("https://www.youtube.com/watch?v=fgXRzjlbbng&list=PLhXQhpqBNAYsiwGQ6e4rxgbQ0gGVfKZ2u&index=3")
        elif a == "angry":
            wb.open("https://www.youtube.com/watch?v=VuDuSrYigTk&list=PLD493513895C1B965")
        elif a == "scared":
            wb.open("https://www.youtube.com/watch?v=ffBgSp6WFg0")
        else:
            wb.open("https://www.youtube.com/watch?v=U4xPahDjY6k")
        break

camera.release()
cv2.destroyAllWindows()
