import cv2
import os

vid = cv2.VideoCapture("/home/sef/Ayvos_Staj/2_frame/vid2.mp4")

try:
    if not os.path.exists('data1'):
        os.makedirs('data1')

except OSError:
    print('Error: Creating directory of data')

currentframe = 0

while (True):
    success, frame = vid.read()

    if success:
        name = './data1/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break

vid.release()
cv2.destroyAllWindows()