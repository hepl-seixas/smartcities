from lcd1602 import LCD1602
from machine import I2C,Pin,ADC,PWM

i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000) #programmation de l'interface I2C utilisé
d = LCD1602 (i2c,2,16) #création de l'objet LCD1602
d.display() #active le LCD

d.print("Hello world") #affichage de Hello world
