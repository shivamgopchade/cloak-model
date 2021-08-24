#red color detection
import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while(True):
    ret,frame=cam.read()

    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #low_green = np.array([25, 52, 72],np.uint8)
                                                 #high_green = np.array([102, 255, 255],np.uint8)
    #frame=cv2.imread("D:/chrome_downloads/stop.png")
    #cv2.imshow("red",frame)
    red_lower1=np.array([0,100,20])
    red_upper1=np.array([10,255,255])
    #hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_lower2 = np.array([160, 100, 20])
    red_upper2 = np.array([180, 255, 255])


    red_mask1 = cv2.inRange(hsv_frame, red_lower1,red_upper1)
    red_mask2=cv2.inRange(hsv_frame,red_lower2,red_upper2)

    red = cv2.bitwise_and(frame, frame, mask=red_mask1+red_mask2)

    cv2.imshow("video",red)

    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()