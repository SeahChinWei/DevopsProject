from hal import hal_moisture_sensor as moisture

moisture.init()

moisture_read = moist.read_sensor()

if (moist.read.sensor()== True):
    #open dome
elif (moist.read.sensor()== False):
    #close dome
