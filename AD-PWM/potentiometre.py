from machine import Pin, ADC
from time import sleep #fonction permettant de faire la même chose que utime.sleep()

led = Pin(16, Pin.OUT) #configuration la pin 20 en sortie
potentiometre = ADC(1) #connexion de la variable potentiometre à la pin A1

while True:
    lecture_potentiometre = potentiometre.read_u16() #permet de lire la valeur de potentiometre codé en 16 bits (unsigned)
    print(lecture_potentiometre) #permet de lire la valeur de potentiometre codé en 16 bits (unsigned)
    if lecture_potentiometre >20000 and lecture_potentiometre< 40000: #si la valeur du potentiometre est entre 2000 et 4000
        led.value(1) #allumage la LED
        sleep(1) #attente d'une seconde
    else:
        led.value(0) #éteignage la LED
        sleep(1) #attente d'une seconde