import time
from datetime import datetime

import cv2 as cv
import numpy as np

# https://docs.opencv.org/4.2.0/d7/dfc/group__highgui.html

INITIAL_FOCUS = 38

# def white_balance(img):
#     result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#     avg_a = np.average(result[:, :, 1])
#     avg_b = np.average(result[:, :, 2])
#     result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
#     result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
#     result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
#     return result

def callback_focus(x):
    """
    Trackbar callback - setting new focus value
    """
    print(f"new focus={x}")
    vc.set(cv.CAP_PROP_FOCUS, x) 
    

def callback_a_inc(x):
    """
    Trackbar callback - incrementing A component offset of LAB colorspace
    """
    print(f"new A increment={x}")
    global a_inc
    a_inc = x


def callback_b_inc(x):
    """
    Trackbar callback - incrementing B component offset of LAB colorspace
    """
    print(f"new B increment={x}")
    global b_inc
    b_inc = x

def setup_ui():
    """
    Setting up window positions and trackbar
    """
    cv.namedWindow("webcam")
    cv.moveWindow("webcam", 0, 0)

    cv.namedWindow("l")
    cv.moveWindow("l", 0, 300)

    cv.namedWindow("a")
    cv.moveWindow("a", 340, 300)

    cv.namedWindow("b")
    cv.moveWindow("b", 680, 300)

    cv.namedWindow("controls")
    # cv.createTrackbar("focus", "controls", int(vc.get(cv.CAP_PROP_FOCUS)), 40, callback_focus)
    cv.createTrackbar("focus", "controls", INITIAL_FOCUS, 40, callback_focus)
    cv.createTrackbar("a_inc", "controls", 0, 255, callback_a_inc)
    cv.createTrackbar("b_inc", "controls", 0, 255, callback_b_inc)

a_inc = 0
b_inc = 0

# initialize the camera
vc = cv.VideoCapture(0)

# Tested resolutions: 160x120 320x240 640x480 800x600 1280x720 (with black side bars)
# vc.set(cv.CAP_PROP_FRAME_WIDTH, 1280) # set the Horizontal resolution
# vc.set(cv.CAP_PROP_FRAME_HEIGHT, 720) # Set the Vertical resolution
vc.set(cv.CAP_PROP_FRAME_WIDTH, 800) # set the Horizontal resolution
vc.set(cv.CAP_PROP_FRAME_HEIGHT, 600) # Set the Vertical resolution
# vc.set(cv.CAP_PROP_FRAME_WIDTH, 640) # set the Horizontal resolution
# vc.set(cv.CAP_PROP_FRAME_HEIGHT, 480) # Set the Vertical resolution
# vc.set(cv.CAP_PROP_FRAME_WIDTH, 320) # set the Horizontal resolution
# vc.set(cv.CAP_PROP_FRAME_HEIGHT, 240) # Set the Vertical resolution

vc.set(cv.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
# Workaround: 
# to apply manual focus initially - read a dummy frame and wait 0.2sec. Next read will have focus set.
# (resolution should be already set and autofocus disabled)
_, _ = vc.read()
time.sleep(0.2)
vc.set(cv.CAP_PROP_FOCUS, INITIAL_FOCUS) # closest focus value is 40

vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 1)
vc.set(cv.CAP_PROP_TEMPERATURE, 5500) #  WB for transparent glass
# vc.set(cv.CAP_PROP_TEMPERATURE, 2800) #  minimum WB - for yellow glass
# print(vc.get(cv.CAP_PROP_TEMPERATURE))
# vc.set(cv.CV_CAP_PROP_SETTINGS, 0)

# with leds 
# vc.set(cv.CAP_PROP_EXPOSURE, -11) # -11 = minimum
vc.set(cv.CAP_PROP_BRIGHTNESS, 50) # 30 = minimum
# vc.set(cv.CAP_PROP_BRIGHTNESS, 160) # 30 = minimum

# # no led highlighting
# vc.set(cv.CAP_PROP_EXPOSURE, 1)
# vc.set(cv.CAP_PROP_BRIGHTNESS, 190)

# # lamp highlighting
# vc.set(cv.CAP_PROP_EXPOSURE, -4)
# vc.set(cv.CAP_PROP_BRIGHTNESS, 30)

setup_ui()

while vc.isOpened():
    # focus = cv.getTrackbarPos("focus", "controls")

    ret, image = vc.read()
    if ret:
        # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.imshow('webcam', image)

        # b, g, r = cv.split(image)
        # cv.imshow('b', b)
        # cv.imshow('g', g)
        # cv.imshow('r', r)

        conv = cv.cvtColor(image, cv.COLOR_BGR2LAB)
        l, a, b = cv.split(conv)
        a[:] += a_inc  # green - red
        b[:] += b_inc  # blue - yellow
        cv.imshow('l', l)
        cv.imshow('a', a)
        cv.imshow('b', b)

        result = cv.merge((l, a, b))
        result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
        cv.imshow('result', result)   

        # conv = cv.cvtColor(image, cv.COLOR_BGR2LAB)
        # conv2 = cv.cvtColor(conv, cv.COLOR_LAB2BGR)
        # cv.imshow('conv', conv)
        # cv.imshow('conv2', conv2)
        
        # cv.imshow('webcam_gr', gray)
        # cv.moveWindow('webcam', 0, 0)
        # cv.moveWindow('webcam_gr', 100, 100)

        # cv.setWindowProperty('webcam', cv.WND_PROP_AUTOSIZE, cv.WINDOW_FULLSCREEN)
        key = cv.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("s"):
            # TODO add millisecond?
            filename = datetime.today().strftime('snapshot_%Y_%m_%d__%H_%M_%S.png')
            cv.imwrite(filename, image)
            print(f"wrote {filename}")
    else:
        break

# cv.destroyWindow('SnapshotTest')
cv.destroyAllWindows()
vc.release()

# if ret:
#     cv.imshow('SnapshotTest', image)
#     cv.waitKey(0)
#     cv.destroyWindow('SnapshotTest')
#     # cv.imwrite('SnapshotTest.jpg',image)
# vc.release()
