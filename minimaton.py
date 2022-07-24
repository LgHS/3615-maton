
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
    webcam.set(3, 160)
    webcam.set(4, 120)

    check, img = webcam.read()
    print('Original size: ', img.shape)

    # resize to fit minitel's dimensions
    dim = (80,60) #*60 to keep aspect ratio and maybe add some text
    img_resized = cv2.resize(img, dim)
    print('Resized: ', img_resized.shape)

    cv2.imwrite(filename='images/camera.jpg', img=img)
    cv2.imwrite(filename='images/camera_resized.jpg', img=img_resized)

    webcam.release()
    to_vdt(check, img_resized)

#####
# to_vdt()
#####
def to_vdt(ret, frame):
    print("converting image...")

    img_bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, img_bitmap = cv2.threshold(img_bw, 127, 255, cv2.THRESH_BINARY)

    tab_byte = []
    byte = ''
    num_pixel = 0
    img_01 = ""
    print('looping each line')
    # loop for each line
    for line in range(31):
        for pixel in range(71):
            pxl_lvl = img_bitmap[line][pixel]

            if(pxl_lvl == 255): # if pixel is black, store as 1
                byte += "1"
                img_01 += "1"
            else: # else, store as 0
                byte += "0"
                img_01 += "0"

            num_pixel +=1
            if (num_pixel%8 ==0):
                tab_byte.append(int(byte,2))
                byte = ""
    print('displaying image')
    display_vdt(img_01)
#####
# Display image to minitel
# display_vdt(image)
#####
def display_vdt(img):
    image = ""
    line_end = 0
    print('building image')
    for pixel in img:
        image += pixel
        line_end += 1
        if (line_end%71 ==0):
            image += "\n"
    image = image.replace('1', '\u2588').replace('0', ' ')
    print(image)
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
