import time
from hal import hal_adc as adc
from hal import hal_led as led

led.init()
adc.init()
while True:
    if (adc.get_adc_value(0)<=500):
        led.set_output(0,1)
    else:
        led.set_output(0,0)
    ldr_value= adc.get_adc_value(0)
    ldr = str(ldr_value)
    print( "LDR value is = " + ldr)
    time.sleep(1)