from ws2812 import WS2812
import utime
from machine import Pin,ADC

black = (0,0,0)
red = (255,0,0)
purple = (180,0,255)
led_neo = WS2812(18,1) #création d'un objet WS2812 prenant en paramètre la pin et le nombre de LED
colors = (black,red,purple)
light_sensor = ADC(2)
while True :
    light = light_sensor.read_u16()
    print (light)
    if light <= 10000:
        led_neo.brightness = 0.05
    else :
        led_neo.brightness = 1
    for i in colors:
        led_neo.pixels_fill (i) #chargement des données
        led_neo.pixels_show() #affichage des couleurs
        utime.sleep(0.2)
    led_neo.rainbow_cycle(0.01) #affichage des couleurs de l'arc en ciel toutes les 0.01 secondes
