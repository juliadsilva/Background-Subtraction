import cv2

cap = cv2.VideoCapture('../Videos/carros.avi')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while 1:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(50)
    if k == 27:
        cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()