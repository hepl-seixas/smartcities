# 0) Introduction
  Une LED RGB est une LED permettant d'afficher plusieurs couleurs. Pour se faire, il faut coder l'intensité de rouge, de vert et de bleu afin d'afficher la couleur    désiré.
  **Remarque** : l'intensité est codé avec un nombre entre 0 et 255.
# 1) méthodes utilisé
  - WS2812(numéro de pin,nombre de led) : Méthode permettant de créer un objet de type WS2812.
  - objetdetypeWS2812.pixels_fill (color) : méthode chargeant la couleur (color) désiré en nombre binaire. Color étant un tuple comprenant les données binaires de éa couleur désiré.
  - objetdetypeWS2812.pixels_show () : méthode affichant la couleur chargé.
  - objetdetypeWS2812.rainbow_cycle(wait) : méthode permettant de changer de couleurs toutes les wait secondes. Cette méthode affichera toutes les couleurs de l'arc en ciel.
# 2) Programme 
```
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
    led_neo.rainbow_cycle(0.01) #affichage des couleurs de l'arc en ciel toutes les 0.01 secondes
```
Il s'agit d'un programme qui affichera les couleurs noir, rouge mauve (avec un espacement de 0.2 secondes) suivit des couleurs de l'arc en ciel avec un changement de couleur toutes les 0.01 secondes.

https://user-images.githubusercontent.com/124899641/230932668-d64f9a08-66e3-429a-b6dd-169f142f7caf.mp4
```
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

```
C'est le même programme sauf qu'il gère la luminosité de la LED à l'aide du capteur de lumière en plus.
