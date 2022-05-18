from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from django.http import HttpResponse
import json

import random

from PIL import Image
from io import BytesIO

import base64

@login_required(login_url="/login/")
def HomeView(request):
    img_str = None
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        print(upload)
        img = Image.open(upload)

        return HttpResponse("success")

    return render(request, 'converter.html', {'output': img_str,

                                              })

