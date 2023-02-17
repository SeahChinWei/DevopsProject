from hal import hal_usonic as ultrasonic
from hal import hal_led as led

ultrasonic.init()
led.init()
#str: dist
    
while True:
    dis = ultrasonic.get_distance()
    #print("distance is "+ dis)
    if (dis<5):
        led.set_output(0,1)
    else:
        led.set_output(0,0)
