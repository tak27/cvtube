import pafy
import cv2

# pip install opencv-python
# pip install pafy
# pip install youtube-dl

url='https://www.youtube.com/watch?v=2TFnNqOQxOQ'
video=pafy.new(url)
print(video.title)
for s in video.streams:
    print(s)
best=video.getbest(preftype='mp4')
print('best: '+str(best))
cap=cv2.VideoCapture(best.url)
while True:
    ret,frame=cap.read()
    cv2.imshow(video.title,frame)
    if cv2.waitKey(20)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
