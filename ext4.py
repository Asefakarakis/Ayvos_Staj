import cv2
import os

vid = cv2.VideoCapture("/home/sef/Ayvos_Staj/4_frame/vid4.mp4")

try:
    if not os.path.exists('data4'):
        os.makedirs('data4')

except OSError:
    print('Error: Creating directory of data')

currentframe = 0
saveframe = 0
while (True):
    success, frame = vid.read()

    if success:
        currentframe += 1
        if (currentframe%4 == 0):
            name = './data4/frame' + str(saveframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            saveframe += 1

    else:
        break

vid.release()
cv2.destroyAllWindows()