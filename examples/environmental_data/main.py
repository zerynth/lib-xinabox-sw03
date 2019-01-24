##############################################
#   This is an example for SW03 ambient
#   temperature, altitude and pressure
#   sensor.
#
#   Ambient temperature, altitude and pressure
#   is measured and printed out on the console.
##############################################
import streams
from xinabox.sw03 import sw03

streams.serial()

# SW03 instance
SW03 = sw03.SW03(I2C0)

# configure SW03
SW03.init()

while True:
    temp = SW03.getTempC()      # return temp in degree celcius
    alt = SW03.getAltitude()    # return alitude in meters
    pres = SW03.getPressure()   # return pressure in pascals
    
    print('Temperature: ', temp, ' C')
    print('Altitude   : ', alt, ' m')
    print('Pressure   : ', pres, ' Pa')
    
    sleep(1000)