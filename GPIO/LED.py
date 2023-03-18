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