import serial
import thread
from SerialControl import *

#Starting Point
ser = serial.Serial (
	baudrate = 19200, 
	port = 'COM8', 
	bytesize = serial.EIGHTBITS, 
	parity = serial.PARITY_NONE, 
	stopbits  = serial.STOPBITS_ONE, 
	timeout = 1
)

if ser.is_open:
	ser.close()
ser.open()
print_port_info(ser)
thread.start_new_thread(log_rx_data, (ser,))
while True: pass

