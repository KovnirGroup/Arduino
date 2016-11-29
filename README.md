# Arduino
Python def for arduino
import serial 
import time
def connectArduino(com, port):
    Arduino = serial.Serial(com, port)
    time.sleep(1)
    return com, port
