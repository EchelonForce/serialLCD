import serial
import time
import socket, struct, fcntl
#Open the serial port for the LCD
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, bytesize=8, parity='N', stopbits=1,  timeout=3.0)
#Create a socket to use when figuring out IP addresses.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd = sock.fileno()
SIOCGIFADDR = 0x8915

#This function determines the IP address of an interface passed in.
def get_ip(iface = 'eth0'):
    ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
    try:
        res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
    except:
        return ""
    ip = struct.unpack('16sH2x4s8x', res)[2]
    return socket.inet_ntoa(ip)

# Main function (get IP addresses and write to screen.
def main():
	clearScreen()
	port.write("W"+get_ip('wlan0').rjust(15))
	port.write("E"+get_ip('eth0').rjust(15))
	#print "wlan0", get_ip('wlan0')
	#print "eth0 ", get_ip('eth0')
	time.sleep(30)

	return

#setup, called once.
def setup():
	#setBacklight( 157 )
	clearScreen()
	return

#Clears the screen by resetting cursor and writing all spaces.
def clearScreen():
	port.write("\xFE\x01")
	port.write("                ")
	port.write("                ")
	port.write("\xFE\x01")
	return

#Set backlight level.
#Requires LCd reboot after wards (stops Rx-ing for some reason).
def setBacklight( val ):
	if val >= 128 and val <= 157 :
		port.write("\x7C")
		port.write(chr(val))
		print "Backlight set to:", val
	else:
		print "ERROR: Backlight not set:", val, "is an invalid value"
	return

#Run setup and infinite loop on main.
setup()
while True:
	main()
