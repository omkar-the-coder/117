import os
import cv2 
path ="Images/"
Images=[]

vid = cv2.videoCapture("AnthonyShkraba.mp4")

if(vid.isOpened9==False):
    print("Unable to read the feed ")

    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(height)
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(width)
    fps = int(vid.get(cv2.CAP_PROP_FRAME_FPS))
    print(fps)

while(True):
    #capture the video frame
    #vy frame
    ret, frame = vid.read()
    
    cv2.imshow("Web cam",frame)

    if cv2.waitkey(1)=32:
        break
 
vid.release ()
cv2.destroyAllWindows   
