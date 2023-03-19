from lcd1602 import LCD1602
from machine import I2C,Pin,ADC,PWM
from utime import sleep

Rotary_angle_sensor = ADC(0) #utilisation de la pin ADC0 pour le potentiomètre
i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000) #programmation de l'interface I2C utilisé
d = LCD1602 (i2c,2,16) #création de l'objet LCD1602
d.display() #active le LCD

while True :
    val_binaire = Rotary_angle_sensor.read_u16() #lit la valeur du potentiomètre 
    d.clear() #effacement de la valeur inscrite dans le LCD
    d.setCursor(0,0) #mise du curseur à la position 0,0
    val_decimal = (val_binaire*300)/65535 #conversion de la valeur du potentiomètre en décimal
    d.print(str(val_decimal)) #affichage de la valeur du potentiomètre
    d.write (0b11011111) # écriture du °
    sleep(1) # repos d'une seconde afin de garder une valeur lisible