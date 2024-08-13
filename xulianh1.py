import cv2
path= r'c:\Users\DELL\Pictures\Camera Roll\0106_hinh-nen-may-tinh-full-hd88.jpg'

img=cv2.imread(path)
cv2.imshow('tai anh',img)
cv2.waitKey(1000)