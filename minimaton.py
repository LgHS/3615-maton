import cv2
webcam = cv2.VideoCapture(0) # Number which capture webcam in my machine
# try either VideoCapture(0) or (1) based on your camera availability
# in my desktop it works with (1)
check, img = webcam.read()
print('Original size: ', img.shape)

# resize to fit minitel's dimensions
dim = (80,60) #*60 to keep aspect ratio and maybe add some text
img_resized = cv2.resize(img, dim)
print('Resized: ', img_resized.shape)

cv2.imwrite(filename='camera.jpg', img=img)
cv2.imwrite(filename='camera_resized.jpg', img=img_resized)
webcam.release()
