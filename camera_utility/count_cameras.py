import cv2

# Get the number of cameras available
def count_cameras():
    max_tested = 100
    for i in range(max_tested):
        # print(f"a{i}")
        # temp_camera = cv2.VideoCapture(i)
        temp_camera = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if temp_camera.isOpened():
            # print(f"b{i}")
            temp_camera.release()
            # cv2.destroyAllWindows()
        else:
            return i

print(f"result={count_cameras()}")

for cam in range(count_cameras()):
    print(cam)