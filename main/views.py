from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse
import json

import random

from PIL import Image
from io import BytesIO

import base64

import pandas as pd

from main import forms

from main import create_model as cm
import os
import numpy as np
import time
from PIL import Image

from django.utils.functional import cached_property
from django.views.decorators.cache import cache_page
from django.core.cache import cache




@login_required(login_url="/login/")
def HomeView(request):

    def create_model():
        model_tokenizer = cm.create_model()
        return model_tokenizer

    form = forms.MainForm
    img_str = None

    df = pd.read_pickle("df_final.pkl")

    if request.method == 'POST' and request.FILES['upload1'] and request.FILES['upload2']:
        form = forms.MainForm(request.POST, request.FILES)

        class TfClass(object):
            @cached_property
            def create_model(self):
                model_tokenizer = cm.create_model()
                return model_tokenizer
        obj = TfClass()

        upload1 = request.FILES['upload1']
        upload2 = request.FILES['upload2']

        def predict(image_1, image_2, model_tokenizer):
            start = time.process_time()

            image_1 = Image.open(image_1).convert("RGB")  # converting to 3 channels
            image_1_array = np.array(image_1) / 255

            image_2 = Image.open(image_2).convert("RGB")  # converting to 3 channels
            image_2_array = np.array(image_2) / 255

            image_index = df[df['image_1'] == str(upload1)].index.values

            pd.set_option('display.max_colwidth', None)
            true_caption = df['impression'][image_index]

            caption = cm.function1([image_1_array], [image_2_array], model_tokenizer)

            output = BytesIO()
            image_1.save(output, format='webp', quality=95)
            output.seek(0)
            image_1_str = base64.b64encode(output.getvalue()).decode()

            output = BytesIO()
            image_2.save(output, format='webp', quality=95)
            output.seek(0)
            image_2_str = base64.b64encode(output.getvalue()).decode()

            time_taken = "Time Taken for prediction: %i seconds" % (time.process_time() - start)

            del image_1_array, image_2_array
            return caption[0], true_caption.values[0], image_1_str, image_2_str

        model_tokenizer = obj.create_model


        caption, true_caption, image_1_str, image_2_str = predict(upload1, upload2, model_tokenizer)

        return render(request, 'index.html', {'image_1_str': image_1_str, 'image_2_str': image_2_str,
                                              'form': form, 'caption': caption, 'true_caption': true_caption,


                                              })
    else:
        return render(request, 'index.html', {'output': img_str,'form':form

                                              })

