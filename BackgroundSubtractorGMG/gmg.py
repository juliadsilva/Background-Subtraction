import cv2

cap = cv2.VideoCapture('../Videos/carros.avi')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while 1:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()