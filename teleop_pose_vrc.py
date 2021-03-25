import cv2
import time
import numpy as np

def unpack_tex(frame):
    block = frame.shape[0]/16
    ix = int(block / 2)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    th, frame_th = cv2.threshold(frame_rgb, 128, 1, cv2.THRESH_BINARY)
    pos = np.array([0, 0, 0])
    for i in range(16):
        iy = int(block / 2 + block * i)
        print(frame_th[iy, ix])
        pos += frame_th[iy, ix] * 2 ** (15 - i)
    pos = (pos - 32768) / 1000
    print(pos)

def main():
    capture = cv2.VideoCapture(1)
    while(True):
        ret, frame = capture.read()
        unpack_tex(frame)
        frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))
        cv2.imshow('title',frame)
        time.sleep(0.05)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()