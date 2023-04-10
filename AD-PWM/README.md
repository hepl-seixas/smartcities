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


https://user-images.githubusercontent.com/124899641/224554092-9999a965-f759-40ca-b54b-cdb4b75d5bc6.mp4



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
  Ce programme va augmenter la luminosité de la LED jusqu'à ce qu'elle atteigne son maximum puis il va baisser la luminosité de la LED jusqu'à ce qu'elle atteigne son minimum. Attention la fréquencede la PWM est importante. Si elle est trop base, l'oeil humain verra la LED clignoté donc il faut que la fréquence soit suffisament élevé
  

https://user-images.githubusercontent.com/124899641/224554203-1fef2bd0-7c97-409f-a4c9-ae896a22a842.mp4


# 3) PWM (Musique)
Un buzzer est un composant électronique permettant de faire de la mesure en alimentant un matériau piezoélectrique.
Il existe 2 type de buzzer :
   - Les buzzers actif sont des buzzers pouvant être alimenté en courant continu et ils générent un son. 
   - Les buzzer passif sont des buzzers alimenté par une PWM ce qui permet de leur faire jouer un son spécifique et donc une musique tout cela en pouvant réglé le volume du son. LA fréquence de la PWM va changé la hauteur d'un son alors que le duty_cycle de la PWM va changer le volume d'un son.
   ##3.1) Descriptions des fonctions
   
   def function name (parameter list):  = syntaxe permettant de créer une fonction
        function body
        
   ##3.2) Exemple de programme
      ![image](https://user-images.githubusercontent.com/124899641/222872829-ff93f28e-7a1d-4107-a093-46e94ca14e47.png)

      ```
      from machine import Pin, PWM
      import utime

      buzzer = PWM(Pin(20))       #Utilisation de la pin 20 comme pin PWM
      def DO (vol, time):         #création des différentes notes joué dans la chanson sous forme de fonction prennant en paramètre leur volume et le temps de jeu
          buzzer.freq (1046)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def RE (vol, time):
          buzzer.freq (1175)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def MI (vol, time):
          buzzer.freq (1318)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def FA (vol, time):
          buzzer.freq (1397)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def SOL (vol, time):
          buzzer.freq (1568)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def LA (vol, time):
          buzzer.freq (1760)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def SI_bemol (vol, time):
          buzzer.freq (1864)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def DO_2 (vol, time):
          buzzer.freq (2043)
          buzzer.duty_u16(vol)
          utime.sleep(time)
      def N():
          buzzer.duty_u16(0) #volume de 0 afin que la dernière note éteigne le son du buzzer
          utime.sleep(0.35)
      DO(1000, 0.35)           #appel des différentes fonctions dans l'ordre afin de créer la musique 
      DO(1000, 0.35)
      RE(1000, 0.35)
      DO(1000, 0.35)
      FA(1000, 0.35)
      MI(1000, 0.35)
      DO(1000, 0.35)
      DO(1000, 0.35)
      RE(1000, 0.35)
      DO(1000, 0.35)
      SOL(1000, 0.35)
      FA(1000, 0.35)
      DO(1000, 0.35)
      DO(1000, 0.35)
      DO_2(1000, 0.35)
      LA(1000, 0.35)
      FA(1000, 0.35)
      MI(1000, 0.35)
      RE(1000, 0.35)
      SI_bemol(1000, 0.35)
      SI_bemol(1000, 0.35)
      LA(1000, 0.35)
      FA(1000, 0.35)
      SOL(1000, 0.35)
      FA(1000, 0.35)
      N()
      ```
   Ce programme va jouer la musique "Happy birthday" en créant une fonction pour chaque note dont les paramètres seront : la fréquence de la note (dépendant de la fréquence de la PWM), le volume de la note (dépendant du duty_cycle de la PWM), du temps pendant lequel la note est joué (paramétré vita un utime.sleep()).


https://user-images.githubusercontent.com/124899641/224554320-4234f505-0b58-44df-a633-f394864600dd.mp4


# 4) PWM (Servo)
Un servomoteur est un moteur s'orientant d'un certain angle (soit entre 0 et 180°, soit entre 0 et 360°) en fonction d'une PWM. Celui du Grove starter kit ne tourne que de 0 à 180°.
Dépendant du servo, il faut des PWM différentes. Voici les valeurs concernant le servo utilisé dans le grove starter kit :
![image](https://user-images.githubusercontent.com/124899641/222873625-ee23a156-9aad-4a65-ae4e-71d93dfee048.png)

   ## 4.1) Descriptions des fonctions
   Il n'y a pas de nouvelles fonctions
   ## 4.2) Exemple de programme
   ![image](https://user-images.githubusercontent.com/124899641/222873643-d9b4f6eb-71e6-4cc4-bff9-2d0c67b77f1f.png)
   ```
from machine import Pin, PWM
import utime

Servo_PWM = PWM (Pin(20))
Servo_PWM.freq(100)
val = 4000
while True :
    while val < 17000: #tant que val ne dépasse la valeur maximale possible donner en PWM. Cet valeur correspond à un angle de 180°
        val=val+1000 #incrémentation de val
        utime.sleep(1)
        Servo_PWM.duty_u16(val) #Envoit la valeur de val en PWM au Servo
    while val>4000:      #tant que val ne dépasse la valeur minimale possible donner en PWM. Cet valeur correspond à un angle de 0°
        val = val-1000 #décrémentation de val
        utime.sleep(1)
        Servo_PWM.duty_u16(val) #Envoit la valeur de val en PWM au Servo
```
Ce programme est quasiment un copier-collé du programme de la LED. C'est parce qu'au niveau de la programmation ces 2 composants fonctionnent de la même manière.
Ce programme va faire tournée plusieurs fois le servo jusqu'à ce qu'il atteigne 180° puis il ira en sens inverse jusqu'à ce qu'il atteigne 0° et ainsi de suite
