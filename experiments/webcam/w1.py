import cv2
from datetime import datetime

# https://docs.opencv.org/4.2.0/d7/dfc/group__highgui.html

# initialize the camera
vc = cv2.VideoCapture(1)

vc.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
vc.set(cv2.CAP_PROP_FOCUS, 35)
# vc.set(cv2.CAP_PROP_WB_TEMPERATURE, 2400)
# print(vc.get(cv2.CAP_PROP_WB_TEMPERATURE))
vc.set(cv2.CAP_PROP_TEMPERATURE, 2800) #  2800 5500
# print(vc.get(cv2.CAP_PROP_TEMPERATURE))
vc.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
# print(vc.get(cv2.CAP_PROP_AUTO_EXPOSURE))

# vc.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
 
# vc.set(cv2.CAP_PROP_EXPOSURE, 15)
# vc.set(cv2.CAP_PROP_BRIGHTNESS, 10)

# vc.set(cv2.CV_CAP_PROP_SETTINGS, 0)

# # with leds 
# vc.set(cv2.CAP_PROP_EXPOSURE, -11) # -11 = minimum
# vc.set(cv2.CAP_PROP_BRIGHTNESS, 30) # 30 = minimum

# # no led highlighting
# vc.set(cv2.CAP_PROP_EXPOSURE, 1)
# vc.set(cv2.CAP_PROP_BRIGHTNESS, 190)

# lamp highlighting
vc.set(cv2.CAP_PROP_EXPOSURE, -4)
vc.set(cv2.CAP_PROP_BRIGHTNESS, 30)

vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # set the Horizontal resolution
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # Set the Vertical resolution

# print(vc.get(cv2.CAP_PROP_FOCUS))
# print(vc.get(cv2.CAP_PROP_AUTO_EXPOSURE))
# print(vc.get(cv2.CAP_PROP_BRIGHTNESS))

while vc.isOpened():
    ret, image = vc.read()
    if ret:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('webcam', image)
        cv2.imshow('webcam_gr', gray)
        cv2.moveWindow('webcam', 0, 0)
        # cv2.moveWindow('webcam_gr', 100, 100)

        # cv2.setWindowProperty('webcam', cv2.WND_PROP_AUTOSIZE, cv2.WINDOW_FULLSCREEN)

        key = cv2.waitKey(1000) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("s"):
            filename = datetime.today().strftime('snapshot_%Y_%m_%d__%H_%M_%S.png')
            cv2.imwrite(filename, image)
            print(f"wrote {filename}")
    else:
        break

# cv2.destroyWindow('SnapshotTest')
cv2.destroyAllWindows()
vc.release()

# if ret:
#     cv2.imshow('SnapshotTest', image)
#     cv2.waitKey(0)
#     cv2.destroyWindow('SnapshotTest')
#     # cv2.imwrite('SnapshotTest.jpg',image)
# vc.release()
