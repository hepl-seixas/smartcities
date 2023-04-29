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
Ce programme va alterner l'affichage de la température et de l'humidité avec l'affichage de la date et du temps sur le LCD toutes les 3 secondes 
![image](https://user-images.githubusercontent.com/124899641/230735789-e24ab416-95e6-4c2e-bf9f-429a124187c2.png)
![image](https://user-images.githubusercontent.com/124899641/230735798-6ba95eb0-4744-4687-a47e-051d88bf3bee.png)

# 2) Capteur de lumière et de son
  ## 0) Introduction 
  Le capteur de son fonctionne à l'aide d'un microphone captant la vibration de l'air et convertissant cette vibration en un signal analogique. Tandis que le capteur de lumière utilise une photorésistance dont la résistance diminue en fonction de l'augmentation de l'intensité lumineuse. Cette partie va en plus introduire l'utilisation d'un ventilateur. Pour le controller, il faut utiliser un driver (le driver utilisé dans ce cours est un driver permettant seulement d'aller vers l'avant) qui sera connecté à un moteur qui sera lui-même connecté au ventilateur
## 1) description des méthodes 
  Il n'y a pas de nouvelles méthodes/fonctions
## 2) programme 
  ```
from lcd1602 import LCD1602
from machine import I2C,Pin,ADC
from utime import sleep

i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000) #programmation de l'interface I2C utilisé
d = LCD1602 (i2c,2,16) #création de l'objet LCD1602
d.display() #active le LCD
light_sensor = ADC(2)
sound_sensor = ADC(0) #connexion des capteurs sur leurs ADC respectifs
fan = Pin(16, Pin.OUT) #configuration la pin 16 en sortie

while True : 
    sound = sound_sensor.read_u16() # lecture des valeurs de température et d'humidité et stockage dans les variables temp et humid
    d.setCursor (0,0)
    d.print ("sound:"+str(sound)) # affichage de l'intensité sonore (en binaire) sur la 1ère ligne du LCD
    d.setCursor (0,1)
    light = light_sensor.read_u16() 
    d.print ("light:"+str(light)) # affichage de l'intensité lumineuse (en binaire ) sur la 2 ème ligne du LCD
    if light >= 40000: #allume ou éteins le ventilateur en fonction de la luminosité
        fan.value(1)
    else:
        fan.value (0)
    sleep (0.3)
```
Ce programme va afficher les valeurs de l'intensité lumineuse et sonore sur un LCD tout en controlant l'activation du ventilateur en fonction de l'intensité lumineuse 



https://user-images.githubusercontent.com/124899641/235323050-8a1c4b25-0a60-4850-a1d1-812abce831e1.mp4



# 3) capteur de mouvement PIR
  ## 0) Introduction 
  Le capteur de mouvement PIR est un capteur détectant les mouvements à l'aide de la lumière infrarouge. Lorsqu'une personne bouge dans son champ de vision, le capteur va détecter une perturbation dans la lumière infrarouge de la pièce ainsi il saura qu'il y a eu un mouvement.
  ## 1) Description des méthodes
   Il n'y a pas de nouvelles méthodes mais ce programme utilise la notion de class. Les class sont très utilisé dans la programmation python, il s'agit de la base de la programmation orienté objet. Un class est un ensemble utilisé lorsque plusieurs objets partagent des mêmes caractéristiques (variables ou fonctions). Afin de créer une class, il faut utiliser le mot clé Class et un constructeur de Class (_init_) ensuite, il suffit de créer toutes les variables/méthodes appartenant à la class.
    
  ## 2) Programme
  ```
  from machine import Pin, PWM
from utime import sleep
class SERVO: 					#création d'une class servo
    def __init__(self, pin):	#appel du constructeur de class
        self.pin = pin			# création de 2 variables d'instances
        self.pwm = PWM(self.pin)
        
    def turn(self, val): #création d'une méthode de la class Servo permettant de touner le moteur d'un angle donné 
        self.pwm.freq(100)
        self.pwm.duty_u16(int(val/180*13000+4000))

servo = SERVO(Pin(20)) # création d'un objet de la classe SERVO
pir = Pin(18,Pin.IN) #connexion du PIR avec la pin 18

while True :
    if pir.value() == 1: # Si le capteur détecter un mouvement, il tourne de 100°
        servo.turn(100)
        print ("mouvement détecté")
        sleep(1)
    else :				# Sinon il tourne de 50°
        servo.turn (50)
        sleep(1)
```
Ce programme va faire tourner un servo moteur en fonction de la détection ou non du capteur PIR 
