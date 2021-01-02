import RPi.GPIO as GPIO
import dht11
import time
import ambient

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

am = ambient.Ambient(12345,'test6789yukkuri')

instance = dht11.DHT11(pin=14)

def main():

    while True:
        result = instance.read()
        if result.is_valid():
            try:
                #send to Ambient
                r=am.send({'d1': result.temperature, 'd2': result.humidity})
                print('sent to Ambient (ret = %d)' % r.status_code)  #result the status code
                print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)

            except requests.exceptions.RequestException as e:
                print('request failed: ', e)
            
            except KeyboardInterrupt:
                print("Cleanup")
                GPIO.cleanup()

        time.sleep(30)

if __name__=="__main__":
    main()
