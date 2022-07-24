import serial
# Read serial port, set baudrate and parity
port = serial.Serial("/dev/ttyUSB0",
        baudrate=4800,
        parity=serial.PARITY_EVEN,
        bytesize=7,
        stopbits=1)

print("Running...")

while True:
    serial = port.read(10) #read one byte
    key = repr(serial)
    key = key[2]

    print(key)
    print(serial)
