import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

try:
	print("\r\n")
	print("----------------------")
	print(" Pico Repeater v1.0.0 ")
	print("----------------------")
 
	while True:
    		led.on()
    		time.sleep(0.2)
    		led.off()
    		time.sleep(0.2)

except KeyboardInterrupt:
	print("CTRL-C received. Rebooting ...")
