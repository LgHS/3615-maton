import cv2
import serial
import time

#####
# Init sequence
#####
def init():
    # Clear screen and position cursor on top left
    port.write(b"\x1b[2J") # Clear screen
    port.write(b"\x1b[H") # Position cursor on top left

    port.write(b"Press space to take a picture\r\n")
    print("Running...")


#####
# Countdown
#####
def countdown():
    time.sleep(1)
    port.write(b"\r3...\r\n")
    time.sleep(1)
    port.write(b"2...\r\n")
    time.sleep(1)
    port.write(b"1...\r\n")
    time.sleep(1)
    port.write(b"Say cheese!\r\n")

#####
# Camera stuff
#####
def camera_handle():
    countdown()
    webcam = cv2.VideoCapture(0) # Number which capture webcam in my machine
    check, img = webcam.read()
    print('Original size: ', img.shape)

    # resize to fit minitel's dimensions
    dim = (80,60) #*60 to keep aspect ratio and maybe add some text
    img_resized = cv2.resize(img, dim)
    print('Resized: ', img_resized.shape)


    cv2.imwrite(filename='images/camera.jpg', img=img)
    cv2.imwrite(filename='images/camera_resized.jpg', img=img_resized)
    webcam.release()


#####
# Serial stuff
#####

# Read serial port, set baudrate and parity
port = serial.Serial("/dev/ttyUSB0",
	baudrate=4800,
	parity=serial.PARITY_EVEN,
	bytesize=7,
	stopbits=1)

init()

while True:
    serial = port.read(1) #read one byte
    key = repr(serial)
    key = key[2]
    #print(key)
    #print(serial)

    if (key == " "):
        camera_handle()


#####
# Chars table
#####
# \x1b[H	Cursor on top left
# \r		Cursor on left
# \n		Line feed
# \x1b[2J	Clear console
