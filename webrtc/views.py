from django.shortcuts import render
import pyscreenshot
from io import BytesIO
from django.http import HttpResponse
import pyautogui
import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'left': 160, 'top': 160, 'width': 200, 'height': 200}




def serve_pil_image(request):
	with mss() as sct:
	    while True:
	        screenShot = sct.grab(mon)
	        img = Image.frombytes(
	            'RGB', 
	            (screenShot.width, screenShot.height), 
	            screenShot.rgb, 
	        )
	        cv2.imshow('test', np.array(img))
	        if cv2.waitKey(33) & 0xFF in (
	            ord('q'), 
	            27, 
	        ):
	            break

	    img_buffer = BytesIO()
	    pyscreenshot.grab().save(img_buffer, 'PNG', quality=50)
	    img_buffer.seek(0)
	    return HttpResponse(img, content_type='image/gif')


def send_js(request,path):
    return flask.send_from_directory('js', path)

# Create your views here.
def audio(request):
	return render(request,'webrtc/a.html')