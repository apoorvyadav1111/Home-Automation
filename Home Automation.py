import RPi.GPIO as GPIO
import time
import Adafruit_DHT
GPIO.setmode(GPIO.BCM)
dht=27
pir_in=4
pir_out=23
ldr_in=17
ldr_out=24
GPIO.setup(pir_in,GPIO.IN)
GPIO.setup(pir_out,GPIO.OUT)
GPIO.setup(ldr_out,GPIO.OUT)
current_state=0
i=0
def rc_time (ldr_in):
    count = 0;

    GPIO.setup(ldr_in, GPIO.OUT)
    GPIO.output(ldr_in, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(ldr_in, GPIO.IN)

    while (GPIO.input(ldr_in) == GPIO.LOW):
        count += 1

    return count
try:
    #Main loop
    while True:
        
        lumens=rc_time(ldr_in)
        print (lumens)
        if (lumens>10000):
            GPIO.output(ldr_out,True)
        else:
            GPIO.output(ldr_out,False)
        
        current_state=GPIO.input(pir_in)    
        if (current_state==1):
            GPIO.output(pir_out,True)
        else:
            GPIO.output(pir_out,False)
        humidity, temperature = Adafruit_DHT.read_retry(11, 27)
        print ("Humidity = {} %; Temperature = {} C".format(humidity,temperature))
        time.sleep(5)
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()





