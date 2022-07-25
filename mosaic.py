import serial
import time
# Read serial port, set baudrate and parity
port = serial.Serial("/dev/ttyUSB0",
        baudrate=4800,
        parity=serial.PARITY_EVEN,
        bytesize=7,
        stopbits=1)

port.write(b'\xff') #solid white
port.write(b'\x20') #solid blank
exit()

#    port.write(b"\x7e")
# print(hex(int('0001110', 2)))

l = 'xxxxxxx'

# count x's
count = len([c for c in l if c == 'x'])

# There will be 2 ^ {count} combinations, so iterate from 0 to 2 ^ {count} - 1
for i in range(2 ** count):
    # Get the binary representation of i
    b = str(bin(i)).replace('0b', '')

    # Pad with zero's so we get {count} digits ('1' becomes '00001')
    b_p = '0' * (count - len(b)) + b

    # Replace x's one at a time
    out = l
    for digit in b_p:
        out = out.replace('x', digit, 1)

    out = hex(int(out,2))
    print(out)

