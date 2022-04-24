import cv2

boy = cv2.imread("boy.jpeg")
gray = cv2.cvtColor(boy,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(gray)
#print(len(face))

for (x,y,w,h) in face :
    cv2.rectangle(boy,(x,y),(x+w,h+y),(255,0,0),2)
    roi_color = boy[y:y+h,x:x+w]
    cv2.imwrite("New_Boy.jpeg",roi_color)

cv2.imshow("Original",boy)
cv2.waitKey(0)
