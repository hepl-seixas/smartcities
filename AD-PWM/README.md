# 0) Introduction
Pour mesurer un signal continu à l'aide d'un microcontrolleur, il faut convertir ce signal en un signal numérique afin d'être codé sur un microcontrolleur. Cela se fait à l'aide d'un ADC (analog to digital converter). Le RPI pico posé sur son shield possède 3 ADC (A0, A1 et A2).

Pour envoyer un signal continu à l'aide d'un microcontroller, il y a 2 solutions :

   - utilisation d'un DAC (digital to analog converter) malheureusement le RPI pico n'en possède pas
   - utilisation de PWM (pulse wide modulation). La PWM est une technologie qui permet au microcontroller d'envoyer des états logique pendant un temps déterminé. La proportion de temps accordé à chaque état logique correspond au duty cycle (= temps à l'état haut / temps à l'état bas) et celui-ci permet donc de calculer une tension moyenne ce qui permet donc de controller plusieurs composants électroniques tel que des LEDs, des Buzzer et des servomoteurs.
![image](https://user-images.githubusercontent.com/124899641/222868211-d61d8278-fc70-4cc0-9c4e-6db3e5acb518.png)

**Remarque** : le RPI pico permet d'utiliser de la PWM avec toutes ses pins GPIO mais il ne possède que 8 générateur de PWM différent se connectant chacun a deux sorties GPIO donc il faut faire attention à prendre des générateur de PWM différents si le projet a besoin de plus qu'une sortie PWM.
# 1) Lecture du potentiomètre
![image](https://user-images.githubusercontent.com/124899641/222856410-1c7761af-a26f-4241-abb2-067206f23fc0.png)
Un potentiomètre est un composant électronique composé de 3 pates et d'une partie rotative permettant de faire varier la résistance entre 2 des 3 pates et donc le voltage entre ces 2 pates. 

##1.1) Descriptions des fonctions
- time.sleep (secondes) = fonction permettant d'attendre un certain nombre de seconde. Il s'agite d'une fonction similaire à utime.sleep(). 
- adc.read_u16() = méthode permetant de lire la valeur de la pin connecté à ADC et de la retourné sous un format de 16 bits.

##1.2) Exemple de programme
![image](https://user-images.githubusercontent.com/124899641/222863779-4a0d5503-7486-4066-93d0-d8b3c17b95fe.png)

```
from machine import Pin, ADC
from time import sleep #fonction permettant de faire la même chose que utime.sleep()

led = Pin(16, Pin.OUT) #configuration la pin 20 en sortie
potentiometre = ADC(1) #connexion de la variable potentiometre à la pin A1

while True:
    lecture_potentiometre = potentiometre.read_u16() #permet de lire la valeur de potentiometre codé en 16 bits (unsigned)
    print(lecture_potentiometre) #permet de lire la valeur de potentiometre codé en 16 bits (unsigned)
    if lecture_potentiometre >20000 and lecture_potentiometre< 40000: #si la valeur du potentiometre est entre 20000 et 40000
        led.value(1) #allumage la LED
        #sleep(1) #attente d'une seconde
    else:
        led.value(0) #éteignage la LED
        #sleep(1) #attente d'une seconde
```
   Ce programme va allumer la LED si le potentiometre est entre 20000 et 40000

# 2) PWM (LED)

   ##2.1) Descriptions des fonctions
   - PWM(Pin(x)) = fonction peremttant l'utilisation de la pin x en PWM
   - PWM(Pin(x)).freq(frequence) = fonction permettant de choisir la fréquence de la PWM. Attention si elle est trop base, un homme verra la LED clignoter
   - PWM(Pin(x)).duty_u16(y) = fonction permettant d'envoyer la valeur de y via PWM à la pin x. Cette donnée sera codé sur 16 bits donc la valeur max est de 65535 (= duty_cycle de 100%)
   ##2.2) Exemple de programme
   ![image](https://user-images.githubusercontent.com/124899641/222870518-0631ca80-cc50-4880-8ec2-3194dd95edce.png)

   ```
   from machine import Pin, PWM
   import utime

   val = 0
   LED_PWM = PWM(Pin(18)) #utilisation de la pin 18 comme pin PWM

   val = 0
   LED_PWM.freq(100) #configuration de la fréquence de la PWM
   while True:
       while val < 65535: #tant que val ne dépasse la valeur maximale possible donner en PWM
           val=val+50 #incrémentation de val
           utime.sleep_ms(1)
           LED_PWM.duty_u16(val) #Envoit la valeur de val en PWM à la LED
       while val>0:      #tant que val ne dépasse la valeur minimale possible donner en PWM
           val = val-50 #décrémentation de val
           utime.sleep_ms(1)
           LED_PWM.duty_u16(val) #Envoit la valeur de val en PWM à la LED
  ```
  Ce programme va augmenter la luminosité de la LED jusqu'à ce qu'elle atteigne son maximum puis il va baisser la luminosité de la LED jusqu'à ce qu'elle atteigne son minimum
# 3) PWM (Musique)

# 4) PWM (Servo)
