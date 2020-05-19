import cv2 as cv
import numpy as np
# https://docs.opencv.org/4.2.0/d7/dfc/group__highgui.html


def white_balance(img):
    result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    avg_a = np.average(result[:, :, 1])
    avg_b = np.average(result[:, :, 2])
    result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
    result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
    return result

cv.namedWindow("webcam")
cv.moveWindow('webcam', 0, 0)

cv.namedWindow("l")
cv.moveWindow("l", 0, 300)

cv.namedWindow("a")
cv.moveWindow("a", 340, 300)

cv.namedWindow("b")
cv.moveWindow("b", 680, 300)

image = cv.imread("sample.png")
image = cv.resize(image, (320, 240))
cv.imshow('webcam', image)
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


# b, g, r = cv.split(image)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)

conv = cv.cvtColor(image, cv.COLOR_BGR2LAB)
l, a, b = cv.split(conv)

# l[:] = 100
a[:] += 10  # green - red
b[:] -= 25  # blue - yellow
# print(b[0][0])
# print(type(b)) # numpy.ndarray
# print(b.shape)
# print(b.size)
# print(b.dtype)

cv.imshow('l', l)
cv.imshow('a', a)
cv.imshow('b', b)

result = cv.merge((l, a, b))
result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
cv.imshow('result', result)

auto_balanced = white_balance(image)
cv.imshow('auto', auto_balanced)

# cv.setWindowProperty('webcam', cv.WND_PROP_AUTOSIZE, cv.WINDOW_FULLSCREEN)
cv.waitKey(0)
        
# cv.destroyWindow('SnapshotTest')
cv.destroyAllWindows()
vc.release()