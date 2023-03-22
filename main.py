import time
import cv2

def video_proc():
    cap = cv2.VideoCapture('sample.mp4')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)


        ret, thresh = cv2.threshold(gray, 105,255, cv2.THRESH_BINARY_INV)

        contours, hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours)>0:
            c = max(contours, key=cv2.contourArea)
            x,y,w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            print("X: ", (x + w)//2)
            print("Y: ", (y + h) // 2)

        cv2.imshow('vid', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1)


video_proc()
cv2.waitKey(0)
cv2.destroyAllWindows

