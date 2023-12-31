import serial
import time

def init():

    arduino = serial.Serial(
        port = '/dev/ttyACM0',
        baudrate = 115200,
        bytesize = serial.EIGHTBITS,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        timeout = 5,
        xonxoff = False,
        rtscts = False,
        dsrdir = False,
        writeTimeout = 2)

    while True:
        try:
            arduino.write("Command from Jetson | ".encode())
            data = arduino.readLine()
            if data:
                print(data)
            time.sleep(1)
        except Exception as e:
            print(e)
            arduino.close()
