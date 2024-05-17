import cv2
video=cv2.VideoCapture('Play.mp4')
currentframe=0
while(True):
    retrn,frame=video.read()
    if retrn:
        cv2.imwrite('img'+str(currentframe)+'.jpg',frame)
        currentframe+=1
    else:
        break
    video.release()
cv2.destroyAllWindows()
