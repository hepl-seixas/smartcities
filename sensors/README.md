# 1) DHT 11

## 0) Introduction
  Le DHT 11 est un capteur de température et d'humidité utilisant une thermistance NTC et un capteur capacitive. Il faut importer la librairie dht11 pour utiliser ce capteur facilement
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
while True :
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
![image](https://user-images.githubusercontent.com/124899641/230735789-e24ab416-95e6-4c2e-bf9f-429a124187c2.png)
![image](https://user-images.githubusercontent.com/124899641/230735798-6ba95eb0-4744-4687-a47e-051d88bf3bee.png)

Ce programme va alterner l'affichage de la température et de l'humidité avec l'affichage de la date et du temps toutes les 3 secondes
# 2) Capteur de lumière et de son
  ## 0) Introduction 
  Le capteur de son fonctionne à l'aide d'un microphone captant la vibration de l'air et convertissant cette vibration en un signal analogique. Tandis que le capteur de lumière utilise une photorésistance dont la résistance diminue en fonction de l'augmentation de l'intensité lumineuse. Cette partie va en plus introduire l'utilisation d'un ventilateur. Pour le controller, il faut utiliser un driver (le driver utilisé dans ce cours est un driver permettant seulement d'aller vers l'avant) qui sera connecté à un moteur qui sera lui-même connecté au ventilateur
## 1) description des méthodes 
  Il n'y a pas de nouvelles méthodes/fonctions
## 2) programme 
  
