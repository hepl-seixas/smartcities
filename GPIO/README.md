Cette section se concentre sur l'utilisation des LED, des boutons poussoir et des interruptions.

# 1) LED

 Cette partie explique comment géré une LED via micropython.
 
 Le module est simple à comprendre : lorsque que la pin digitale est à l'état haut, la LED s'allume et inversément
 
## a) description des fonctions :
 
   - Pin(num,Pin.OUT/IN) = fonction permettant de mettre une pin en imput ou en output
   - p2 = Pin(num, Pin.IN, Pin.PULL_UP) = fonction permettant d'attacher une résistance de pull-up à une pin
   - p0.value(0)/p0.value(1) = fonction permettant de donner une valeur à une pin
   - p0.value() = fonction permettant de lire la valeur d'une pin 
   - pin.toogle() = fonction permettant d'alterner l'état de la pin.
   - utime.sleep (secondes) = fonction permettant d'attendre un certain temps
   - utime.sleep_ms(milisecondes)
   
## b) Exemple de code :
    
  ```
  from machine import Pin # c'est une librairie permettant d'accéder à des éléments propres à l'hardware (CPU, timer, bus, ...)
  import utime # c'est une librairie permettant de controller le temps dans notre projet

  led = Pin(20, Pin.OUT) #configuration la pin 20 en sortie

  led.value (1) # allumage de la LED
  utime.sleep (1) #attente d'une seconde
  led.value (0) #éteignage de la LED
  utime.sleep (1)
  while True :
      led.toggle() #alternance des état de la LED
      utime.sleep_ms(500) #attente de 500ms
 ```
 

https://user-images.githubusercontent.com/124899641/224553579-893817a6-990a-4205-a3d0-e9341e6860fa.mp4


# 2) bouton-poussoir
  Cette partie explique comment géré une bouton-poussoir via micropython.
  
  Le module est simple à comprendre : lorsque que le bouton est pressé, il retourne la valeur 1 et inversément
   
## a) description des fonctions :
   Il n'y a pas de nouvelles fonctions



## b) Exemple de code :
```
  from machine import Pin
  import utime

  led = Pin(20, Pin.OUT) #configuration la pin 20 en sortie
  bouton = Pin (19, Pin.IN) #configuration de la pin 19 en sortie
  val = 0
  while True :
      if bouton.value() == 1 : #test de la valeur du bouton
          val = val + 1        
          utime.sleep(1)
      elif val == 2 :         #test de si le bouton a été pressé une 2ème fois
          val = 0
          utime.sleep(1)
      led.value(val)
 ```
 Ce programme permet d'allumer/éteindre la LED quand le bouton est pressé. 



https://user-images.githubusercontent.com/124899641/224553636-5acf2f42-f048-497c-a189-3aab586c9ca8.mp4


