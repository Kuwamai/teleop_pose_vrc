import cv2

capture = cv2.VideoCapture(1)

while(True):
    ret, frame = capture.read()
    frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))
    cv2.imshow('title',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()