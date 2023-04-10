from ws2812 import WS2812
import utime

black = (0,0,0)
red = (255,0,0)
purple = (180,0,255)
led_neo = WS2812(18,1) #création d'un objet WS2812 prenant en paramètre la pin et le nombre de LED
colors = (black,red,purple)
while True :
    for i in colors:
        led_neo.pixels_fill (i) #chargement des données
        led_neo.pixels_show() #affichage des couleurs
        utime.sleep(0.2)
    led_neo.rainbow_cycle(0.01)
