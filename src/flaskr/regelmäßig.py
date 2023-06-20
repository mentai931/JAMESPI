import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
from datetime import date, datetime
from flaskr.db import get_db, close_db


DHTPin = 11     #define the pin of DHT11

def measure():
    GPIO.setwarnings(False)
    try:
        dht = DHT.DHT(DHTPin)   #create a DHT class object



        today = date.today().strftime("%B %d. %Y")
        currentTime = datetime.now().strftime("%H:%M:%S")

        for i in range(0,15):            
            chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print("DHT11,OK!")
                break
            time.sleep(0.1)

        temperature = dht.temperature
        humidity = dht.humidity
        currentDate = datetime.datetime.now()

        insertQuery = "INSERT INTO BoxData VALUES (?,?,?);"

        db = get_db()
        db.execute(insertQuery, (temperature, humidity, currentDate))
        db.commit()
        db.close_db()
        
        

    finally:
        GPIO.cleanup
        
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        measure()
        exit()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()  
