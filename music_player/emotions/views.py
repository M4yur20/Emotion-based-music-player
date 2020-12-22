from django.shortcuts import render
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
    form = PredictionForm(request.data, request.FILES)
    if form.is_valid():
        ins = form.save(commit=False)
        image = cv2.imread(ins.image.path, 0)
        faces = face_classifier.detectMultiScale(image, 1.3, 5)
