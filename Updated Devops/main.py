from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_rfid_reader as rfid_reader
from hal import hal_adc as adc
from hal import hal_dc_motor as dc
from hal import hal_temp_humidity_sensor as dht
from hal import hal_servo as servo
from hal import hal_usonic as ultrasonic
from hal import hal_moisture_sensor as moisture
import requests
import time

def main():

    # Get lcd instance
    lcd = LCD.lcd()
    
    # initialize HAL driver
    led.init()
    adc.init()
    dc.init()
    dht.init()
    servo.init()
    ultrasonic.init()
    moisture.init()
    reader = rfid_reader.init()

    #initialize variables
    auth_card = '369693405083'
    lcd.backlight(1)
    lcd.lcd_clear()
    led.set_output(0, 0);
    url = "https://api.thingspeak.com/update.json"
    api_key = "WPWE7B2G1V5C4J5O"
    url2 = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update"
    api_key2 = "HL2SN9W4BK45PQ9K"

    # Infinite loop to scan for RFID cards
    while True:

        #Retrieve water level
        [Temperature, Humidity] = dht.read_temp_humidity()
        id = reader.read_id_no_block()
        id = str(id)
        dis = ultrasonic.get_distance()
        
        # Display message on LCD
        lcd.lcd_display_string("Tap RFIF cards", 1)

        #pH level of the solution
        if (adc.get_adc_value(1)<500):
            #dc.set_motor_speed(20)
            servo.set_servo_position(20)
            lcd.lcd_display_string("pH level is low",2)
            time.sleep(2)
            lcd.lcd_display_string("                    ",2)
            
        elif(adc.get_adc_value(1)>=700):
            #dc.set_motor_speed(0)
            lcd.lcd_display_string("pH level is High",2)
            time.sleep(2)
            lcd.lcd_display_string("                    ",2)
            
        #Ambient light intensity
            #multithreading added
        if (adc.get_adc_value(0)<=700):
            led.set_output(0,1)
            #lcd.lcd_display_string("solution is added", 2)
            
        elif (adc.get_adc_value(0)>700):
            led.set_output(0,0)
            ldr_value= adc.get_adc_value(0)
            ldr = str(ldr_value)
            print( "LDR value is = " + ldr)
            time.sleep(1)
            
        #EC(Electrical Conductivity) level
        if (moist.read.sensor()== True):
            servo.set_servo_position(20)
            lcd.lcd_display_string("EC is low",2)
            time.sleep(2)
            lcd.lcd_display_string("                    ",2)
            
        elif (moist.read.sensor()== False):
            servo.set_servo_position(0)

        #Pump to increase water
        if (dis<5):
            dc.set_motor_speed(20)
            time.sleep(2)
            lcd.lcd_display_string("Pump is on",2)
            
        elif(dis>=5):
            dc.set_motor_speed(0)
            
        #Ambient Temperature and Humidity
        if (Temperature>38) or (Humidity<90):
            #servo.set_servo_position(20)
            dc.set_motor_speed(20)
            lcd.lcd_display_string("Fan is turned on",2)
            time.sleep(2)
            lcd.lcd_display_string("                    ",2)

        #Tagging the yield
        if id != "None" and id==auth_card:
            #print("RFID card ID = " + id)
            print ("carrot")
            
            # Display RFID card ID on LCD line 2
            lcd.lcd_display_string("carrot",2)
            time.sleep(1)
            lcd.lcd_display_string("                    ",2)

        #Sending data to thingSpeak
        data = {'field1': Temperature, 'field2': Humidity, 'field3': dis, 'field4': ldr}
        response = requests.post(url, params={'api_key': api_key}, json=data)
        if response.status_code == 200:
            print("Data sent to ThingSpeak successfully.")
        elif response.status_code != 200:
            print("Error sending data to ThingSpeak.")

        #response2 = requests.post(url2, data={'api_key': api_key2, 'status': message})

        #if response2.status_code == 200:
            #print("Tweet sent to ThingTweet successfully.")
        #else:
            #print("Error sending tweet to ThingTweet.")

#Main entry point
if __name__ == "__main__":
    main()
