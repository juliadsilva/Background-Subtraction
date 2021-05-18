import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

imgo = cv2.imread('../Imagens/img.jpg')
height, width = imgo.shape[:2]

mask = np.zeros(imgo.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (10, 10, width-30, height-30)
cv2.grabCut(imgo, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img1 = imgo*mask[:, :, np.newaxis]

background = imgo-img1

background[np.where((background > [0, 0, 0]).all(axis=2))] = [255, 255, 255]

final = background + img1

cv2.imshow('image', final)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()