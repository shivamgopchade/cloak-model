import numpy as np
import cv2

cam=cv2.VideoCapture(0)
kernal=np.ones([3,3],np.uint8)

ret,img=cam.read()
img=cv2.resize(img,(0,0),fx=2,fy=2)

#img=np.flip(img,axis=1)

#img1=np.flip(img1,axis=1)
while True:

    ret,frame=cam.read()
    frame=cv2.resize(frame,(0,0),fx=2,fy=2)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower1=np.array([0,100,20])
    upper1=np.array([10,255,255])

    lower2=np.array([160,100,20])
    upper2=np.array([180,255,255])

    low_green = np.array([25, 52, 72],np.uint8)
    high_green = np.array([102, 255, 255],np.uint8)

    mask1=cv2.inRange(hsv_frame,lower1,upper1)
    mask2=cv2.inRange(hsv_frame,lower2,upper2)

    #mask=cv2.inRange(hsv_frame,low_green,high_green)
    mask=mask1+mask2
    #mask=cv2.dilate(mask,kernal,3)
    filter_frame=cv2.bitwise_and(frame,frame,mask=255-mask)

    cloak_frame=cv2.bitwise_and(img,img,mask=mask)

    final_frame=cv2.bitwise_or(filter_frame,cloak_frame)

    cv2.imshow("filter",final_frame)


    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()