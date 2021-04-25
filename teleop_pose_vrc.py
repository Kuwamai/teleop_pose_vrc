import cv2
import time
import numpy as np
import sys
import roslibpy

def unpack_tex(frame):
    block = frame.shape[0]/16
    ix = int(block / 2)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    th, frame_th = cv2.threshold(frame_rgb, 128, 1, cv2.THRESH_BINARY)
    pos = np.array([0, 0, 0])
    for i in range(16):
        iy = int(block / 2 + block * i)
        pos += frame_th[iy, ix] * 2 ** (15 - i)
    pos = (pos - 32768) / 1000
    return pos

def main():
    ip_address = sys.argv[1]
    client = roslibpy.Ros(ip_address, 9090)
    client.run()

    topic_name = "/arm_pose"
    message_type = "geometry_msgs/Pose"
    talker = roslibpy.Topic(client, topic_name, message_type)

    capture = cv2.VideoCapture(1)
    while(True):
        ret, frame = capture.read()
        pos = unpack_tex(frame)
        print(pos)
        talker.publish(roslibpy.Message({
            "position": {
                "x": pos[2],
                "y": -pos[0],
                "z": pos[1]
            },
            "orientation": {
                "x": 0,
                "y": 0,
                "z": 0,
                "w": 1
            }
        }))

        frame = cv2.resize(frame, (frame.shape[1], frame.shape[0]))
        cv2.imshow('title',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.05)

    talker.unadvertise()
    client.terminate()
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()