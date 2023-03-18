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
    