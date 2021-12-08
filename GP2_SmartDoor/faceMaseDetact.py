import numpy as np
import cv2  
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from time import sleep


with_mask = np.load('with_mask.npy')
without_mask = np.load('without_mask.npy')


with_masks = with_mask.reshape(200,50*50*3)
without_masks = without_mask.reshape(200,50*50*3)


X = np.r_[with_masks, without_masks]

labels = np.zeros(X.shape[0])
labels[200:] = 1.0

x_train, x_test, y_train, y_test = train_test_split(X,labels, test_size=0.35)

pca = PCA(n_components=3)
x_train = pca.fit_transform(x_train)
x_test = pca.fit_transform(x_test)

svm = SVC()
svm.fit(x_train, y_train)
y_pred = svm.predict(x_test)

def faceMaskDetacted ():
    haar_data = cv2.CascadeClassifier('data.xml')
    result = -1
    capture = cv2.VideoCapture(0)
    data_withmask = []
    value = { 0 : 'With Mask ' , 1 : 'No Mask'}
    font = cv2.FONT_HERSHEY_COMPLEX
    while True:
        flag, img = capture.read()
        if flag:
            faces = haar_data.detectMultiScale(img)
            for x,y,w,h in faces:
                face = img[y:y+h, x:x+w, :]
                face = cv2.resize(face, (50,50))
                face = face.reshape(1,-1)
                face = pca.transform(face)
            # 0 is withMask , 1 withoutMask
                pred = svm.predict(face)
                vl = value[int(pred)]
                if int(pred) == 0:
                    result =0
                    cv2.rectangle(img, (x, y), (x + w, y + h), (107, 205, 42), 4)
                    cv2.putText(img, vl, (x,y), font, 1 , (42,205,91) , 2)
                else:
                    result = 1
                    cv2.rectangle(img, (x, y), (x + w, y + h), (18, 18, 243), 4)
                    cv2.putText(img, vl, (x, y), font, 1, (13, 13, 284), 2)
            cv2.imshow('result', img)
            if cv2.waitKey(2) == 27 or len(data_withmask) >= 200:    
                break
            sleep(5)
            break
    capture.release()
    cv2.destroyAllWindows()
    return result
