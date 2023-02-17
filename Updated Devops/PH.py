import time
from hal import hal_adc as adc
from hal import hal_servo as servo
from hal import hal_lcd as LCD

adc.init()
servo.init()
lcd = LCD.lcd()

lcd.backlight(1)
lcd.lcd_clear()

while True:
    print(adc.get_adc_value(1))
    if (adc.get_adc_value(1)<500):
        lcd.lcd_display_string("Pump is turned on", 1)
        servo.set_servo_position(0)
        servo.set_servo_position(45)
        servo.set_servo_position(90)
        servo.set_servo_position(135)
        servo.set_servo_position(180)
        time.sleep(5)