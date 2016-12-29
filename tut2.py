"""
TUT2: capture a picture with PiCamera
"""

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

# assign the PiCamera object
camera = PiCamera()

# start previewing the camera
camera.start_preview()
# we need atleast 2 seconds for the camera stabilize
time.sleep(2.2)

# take a picture
camera.capture("/home/pi/Desktop/imgs/raw.jpg")
# wait a moment for the camera stabilize again
time.sleep(0.1)

# create an annotation text
camera.annotate_text = "hello world"
camera.capture("/home/pi/Desktop/imgs/annotate.jpg")
time.sleep(0.1)

# change brightness, 0 - 100, default = 50
camera.brightness = 70
camera.capture("/home/pi/Desktop/imgs/br1.jpg")
time.sleep(0.1)
camera.brightness = 50

# change contrast, 0 - 100, default = 50
camera.contrast = 80
camera.capture("/home/pi/Desktop/imgs/con1.jpg")
camera.contrast = 50
time.sleep(0.1)

# some affect, store in camera.IMAGE_EFFECTS
# negative, solarize, sketch, denoise, emboss, oilpaint, hatch gpen, pastel
# watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, colorbalance, cartoon
# deinterlace1, deinterlace2.
camera.image_effect = "colorswap"
camera.capture("/home/pi/Desktop/imgs/effect1.jpg")
time.sleep(0.1)
camera.image_effect = "none"

# auto white balance in camera.awb_mode (camera.AWB_MODES)
# off, auto, sunlight, cloudy, shade, tungsten, fluorescent
# incandescent, flash, horizon

# exposure mode in camera.exposure_mode (camera.EXPOSURE_MODES)
# off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps
# antishake, fireworks


# recording video, comment the above parts to make camera record video
# video can only be save in h264 format

# camera.start_recording("/home/pi/Desktop/imgs/vid.h264")
# time.sleep(10) #recording for 10 second
# camera.start_recording()

camera.stop_preview()
