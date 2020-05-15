import cv2

# initialize the camera
vc = cv2.VideoCapture(1)

vc.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
vc.set(cv2.CAP_PROP_FOCUS, 35)
# vc.set(cv2.CAP_PROP_WB_TEMPERATURE, 2400)
# print(vc.get(cv2.CAP_PROP_WB_TEMPERATURE))
vc.set(cv2.CAP_PROP_TEMPERATURE, 2800) #  2800 5500
# print(vc.get(cv2.CAP_PROP_TEMPERATURE))
vc.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
print(vc.get(cv2.CAP_PROP_AUTO_EXPOSURE))

# vc.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
 
# vc.set(cv2.CAP_PROP_EXPOSURE, 15)
# vc.set(cv2.CAP_PROP_BRIGHTNESS, 10)

# vc.set(cv2.CV_CAP_PROP_SETTINGS, 0)

# with leds 
# vc.set(cv2.CAP_PROP_EXPOSURE, -11) # -11 = minimum
vc.set(cv2.CAP_PROP_EXPOSURE, -13) # -11 = minimum
vc.set(cv2.CAP_PROP_BRIGHTNESS, 30) # 30 = minimum

# # no led highlighting
# vc.set(cv2.CAP_PROP_EXPOSURE, 1)
# vc.set(cv2.CAP_PROP_BRIGHTNESS, 190)

vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # set the Horizontal resolution
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # Set the Vertical resolution

# print(vc.get(cv2.CAP_PROP_FOCUS))
# print(vc.get(cv2.CAP_PROP_AUTO_EXPOSURE))
# print(vc.get(cv2.CAP_PROP_BRIGHTNESS))


ret, image = vc.read()

if ret:
    cv2.imshow('SnapshotTest', image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    # cv2.imwrite('SnapshotTest.jpg',image)
vc.release()
