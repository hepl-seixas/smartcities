Cette section se concentre sur l'utilisation des LED, des boutons poussoir et des interruptions.

## 1) LED
 a) description des fonctions :
 
   - Pin(num,Pin.OUT/IN) = fonction permettant de mettre une pin en imput ou en output
   - p2 = Pin(num, Pin.IN, Pin.PULL_UP) = fonction permettant d'attacher une résistance de pull-up à une pin
   - p0.value(0)/p0.value(1) = fonction permettant de donner une valeur à une pin
   - p0.value() = fonction permettant de lire la valeur d'une pin 
   - pin.toogle() = fonction permettant d'alterner l'état de la pin.
   - utime.sleep (secondes) = fonction permettant d'attendre un certain temps
   - utime.sleep_ms(milisecondes)
   
   b) Exemple de code :
    
  ```
  from machine import Pin
  import utime

  led = Pin(20, Pin.OUT) #configuration la pin 20 en sortie

  led.value (1) # allumage la LED
  utime.sleep (1) #attente une seconde
  led.value (0) #éteignage la LED
  utime.sleep (1)
  while True :
      led.toggle() #alternance des état de la LED
      utime.sleep_ms(500) #attente de 500ms
 ```
