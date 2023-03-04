# 0) Introduction
Pour mesurer un signal continu à l'aide d'un microcontrolleur, il faut convertir ce signal en un signal numérique afin d'être codé sur un microcontrolleur. Cela se fait à l'aide d'un ADC (analog to digital converter). Le RPI pico posé sur son shield possède 3 ADC (A0, A1 et A2).



# 1) Lecture du potentiomètre
![image](https://user-images.githubusercontent.com/124899641/222856410-1c7761af-a26f-4241-abb2-067206f23fc0.png)
Un potentiomètre est un composant électronique composé de 3 pates et d'une partie rotative permettant de faire varier la résistance entre 2 des 3 pates et donc le voltage entre ces 2 pates. 
```
from machine import Pin, ADC
from time import sleep #fonction permettant de faire la même chose que utime.sleep()

led = Pin(20, Pin.OUT) #configuration la pin 20 en sortie
potentiometre = ADC(1) #connexion de la variable potentiometre à la pin A1

while True:
    lecture_potentiometre = potentiometre.read_u16() #permet de lire la valeur de potentiometre codé en 16 bits (unsigned)
    print(lecture_potentiometre) #permet de lire la valeur de potentiometre codé en 16 bits (unsigned)
    if lecture_potentiometre >20000 and lecture_potentiometre< 40000: #si la valeur du potentiometre est entre 2000 et 4000
        led.value(1) #allumage la LED
        #sleep(1) #attente d'une seconde
    else:
        led.value(0) #éteignage la LED
        #sleep(1) #attente d'une seconde
```

# 2) PWM (LED)

# 3) PWM (Musique)

# 4) PWM (Servo)
