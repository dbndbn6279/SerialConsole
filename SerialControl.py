import thread
def print_port_info(port):
	print "Port: " + str(port.port)
	print "Baudrate: " + str(port.baudrate)
	print "Bytesize: " + str(port.bytesize)
	print "Stopbits: " + str(port.stopbits)
	if port.is_open:
		print "Port Status: ON"
	else:
		print "Port Status: OFF"

def log_rx_data(port):
	while True:
		s = port.readline()
		if len(s) != 0: print s
