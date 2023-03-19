# 0) Introduction
LCD (liquid-crystal display) est un type d'écran très utilisé en électronique afin d'afficher certaines données/messages. 

Il se base sur la technologie des cristaux liquides. Il s'agit d'une matière qui possède des indices de réfractions différents lorsque des champs électriques d'intensité différentes lui sont appliqués. 

![image](https://user-images.githubusercontent.com/124899641/226145374-66aa62e2-760a-4de3-b1dd-b114dd019d25.png)

Ainsi, il suffit d'avoir une source de lumière émettant sa lumière sur des cristaux liquides afin de changer la réfraction de la lumière et donc le message affiché sur l'écran LCD.

L'écran LCD utilisé dans ce github est un écran possèdant 2 lignes et 16 colones.

Afin de programmer l'écran LCD, il est conseillé d'utiliser une bibliothèque afin de se siplifier la vie. Pour l'utiliser, il suffit d'enregister le fichier bibliothèque LCD (https://github.com/TinkerGen/Pico-micropython) directement sur le raspberry pie.

# 1) Description des méthodes

La librairie LCD téléchargé précédement est une librairie orienté objet donc il s'agit d'une librairie avec une classe (LCD1602) et des méthodes qui lui sont associés. Cdtte partie va décrire les différentes méthodes existantes dans cette librairie.

• display() — Active l'afficheur.

• no_display() — désactive l'afficheur.

• clear() — supprime ce qui est affihé et renvoit le curseur.

• setCursor(col, row) — choisit l'endroit où le curseur doit se positionner. Row = la ligne et col = la colonne.

• print(text) — Affiche les caractères. Cette méthode n'accepte que le format des chaines de caractères donc il ne faut pas oublier de changer le type d'une variable afin de pouvoir utiliser cette méthode.

• machine.I2C(id,*,scl,sda,freq=400000) — Il s'agit d'une méthode permettant de programmer l'interface I2C utilisé avec le LCD. id = numéro du périphérique I2C utilisé, scl = pin utilisé pour le SCl de l'I2C, SDA = pin utilisé pour le SDA de l'I2C, freq = la fréquence maximale utilisé par la pin SCL.

• d = LCD1602 (i2c,2,16) — création d'un objet de type LCD1602. Les paramètres correspondent au type de liaison utilisé, nombre de colone et nombre de ligne.

# 2) Programmes
Cette partie se consacra sur la programmation de 2 programmes permettant : d'afficher un message/la position angulaire d'un potentiomètre sur un LCD

  ## 2.1) Affichage de messages sur le LCD
  ```
  from lcd1602 import LCD1602
  from machine import I2C,Pin,ADC,PWM

  i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000) #programmation de l'interface I2C utilisé
  d = LCD1602 (i2c,2,16) #création de l'objet LCD1602
  d.display() #active le LCD

  d.print("Hello world") #affichage de Hello world
```
  ## 2.2) Affichage de la position angulaire du potentiomètre
