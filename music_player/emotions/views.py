from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
# Create your views here.
import numpy as np
from keras.models import model_from_json
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
import cv2
from .forms import *

json_file = open(r'C:\Users\mishr\Downloads\model786.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(r'C:\Users\mishr\Downloads\model786.h5')
loaded_model.compile(loss=categorical_crossentropy,
                     optimizer=Adam(lr=0.001),
                     metrics=['accuracy'])
face_classifier = cv2.CascadeClassifier(r'C:\Users\mishr\haarcascade_frontalface_alt.xml')

@require_POST
def predict(request):
    form = PredictionForm(request.POST,request.FILES)
    print(form.is_valid())
    if form.is_valid():
        ins = form.save()
        print(ins.image.path)
        image = cv2.imread(ins.image.path, 0)
        faces = face_classifier.detectMultiScale(image, 1.3, 5)
        print(len(faces))
        for (x,y,w,h) in faces:
       
            roi_gray=image[y:y+h,x:x+w]
            if roi_gray.shape[0]>250 or roi_gray.shape[1]>250:
                roi_gray=cv2.resize(roi_gray,(250,250),interpolation=cv2.INTER_AREA)
            else:
                roi_gray=cv2.resize(roi_gray,(250,250),interpolation=cv2.INTER_CUBIC)
            roi_gray=np.array(roi_gray,'float32')
            roi_gray/=255
            label=loaded_model.predict(roi_gray.reshape(-1,250,250,1))
            emotion=np.argmax(label[0])
            return redirect('playlist:emotion',type=emotion)
    else:
        return redirect('startpage')    