

import cv2
import matplotlib.pyplot as plt
import numpy as np
import subprocess



haar_data = cv2.CascadeClassifier('data.xml')


capture = cv2.VideoCapture(0)
data_withmask = []
while True:
    flag, img = capture.read()
    if flag:
        faces = haar_data.detectMultiScale(img)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w , y+h), (255,0,255), 4)
            face = img[y:y+h, x:x+w, :]
            face = cv2.resize(face, (50,50))
            print(len(data_withmask))
            if len(data_withmask) < 400:
                data_withmask.append(face)
        cv2.imshow('result', img)
        if cv2.waitKey(2) == 27 or len(data_withmask) >= 200:
            break
capture.release()
cv2.destroyAllWindows()

np.save('with_mask.npy', data_withmask)
