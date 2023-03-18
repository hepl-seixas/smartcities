from machine import Pin, PWM
import utime

val = 0
LED_PWM = PWM(Pin(18)) #utilisation de la pin 18 comme pin PWM

val = 0
LED_PWM.freq(100) #configuration de la fréquence de la PWM
while True:
    while val < 65535: #tant que val ne dépasse la valeur maximale possible donner en PWM
        val=val+50 #incrémentation de val
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val) #Envoit la valeur de val en PWM à la LED
    while val>0:      #tant que val ne dépasse la valeur minimale possible donner en PWM
        val = val-50 #décrémentation de val
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val) #Envoit la valeur de val en PWM à la LED