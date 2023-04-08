# 1) DHT 11

## 0) Introduction

## 1) description des méthodes 
  - DHT (20) : création de l'objet DHT et affectation de l'objet à la pin 20
  - machine.RTC() : création de l'objet RTC permettant d'afficher la date et l'heure
## 2) programme 
```
from lcd1602 import LCD1602
from machine import I2C,Pin,ADC,PWM,RTC
from dht11 import *
from utime import sleep

i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000) #programmation de l'interface I2C utilisé
d = LCD1602 (i2c,2,16) #création de l'objet LCD1602
d.display() #active le LCD
dht = DHT (20) # affectation de la pin 20 au capteur d'humidité et de température
rtc = machine.RTC()

for i in range (0,3,1) :
    temp, humid = dht.readTempHumid() # lecture des valeurs de température et d'humidité et stockage dans les variables temp et humid
    d.setCursor (0,0)
    d.print ("Temp:"+str(temp)) # affichage de la température sur la 1ère ligne du LCD
    d.setCursor (0,1)
    d.print ("Humid:"+str(humid)) # affichage de l'humidité sur la 2 ème ligne du LCD
    sleep (1)
    
for i in range (0,3,1) :
    print (rtc.datetime())
    d.setCursor (0,0)
    d.print ("date:"+str(rtc.datetime()[2]) + "/" + str(rtc.datetime()[1]) + "/" + str(rtc.datetime()[0])) # affichage de la date sur la 1ère ligne
    d.setCursor (0,1)
    d.print ("time:"+str(rtc.datetime()[4]) + "h" + str(rtc.datetime()[5])) # affichage du temps sur la 2ème ligne
    sleep (1)
```
