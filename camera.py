import cv2
import time

vid = cv2.VideoCapture(1)
prev_time = time.time()
delay = 5

while(True):
    ret, frame = vid.read()

    if (time.time()-prev_time > delay):
        cv2.imshow('frame', frame)
        prev_time = time.time()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()