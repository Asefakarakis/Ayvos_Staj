import cv2
import os

vid = cv2.VideoCapture("/home/sef/Ayvos_Staj/3_frame/vid3.mp4")

try:
    if not os.path.exists('data3'):
        os.makedirs('data3')

except OSError:
    print('Error: Creating directory of data')

currentframe = 0
saveframe = 0
while (True):
    success, frame = vid.read()

    if success:
        currentframe += 1
        if (currentframe%3 == 0):
            name = './data3/frame' + str(saveframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            saveframe += 1

    else:
        break

vid.release()
cv2.destroyAllWindows()