from hal import hal_dc_motor as dc
from hal import hal_temp_humidity_sensor as dht
from hal import hal_lcd as LCD
import time

dc.init()
dht.init()
lcd = LCD.lcd()
lcd.backlight(1)
lcd.lcd_clear()

while True:
    [Temperature, Humidity] = dht.read_temp_humidity()
    print(Temperature, Humidity)
    if (Temperature>24) or (Humidity>80):
        dc.set_motor_speed(20)
        lcd.lcd_display_string("Fan is turned on", 1) 
    else:
        dc.set_motor_speed(0)
    time.sleep(1)
