import cv2 

#reading the image and storing it to a variable img
img = cv2.imread("solar-system.jpg")

#adding text below or above the planets and beside the sun
cv2.putText(img,'mercury',(115,185),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'venus',(190,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'earth',(287,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'mars',(380,255),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'jupiter',(600,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'saturn',(750,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'uranus',(965,285),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'neptune',(1110,285),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'sun',(100,50),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,150))

#showing the image as output
cv2.imshow("output", img)

#saving the final image
cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)