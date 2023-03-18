from machine import Pin, PWM
import utime

Servo_PWM = PWM (Pin(20))
Servo_PWM.freq(100)
val = 4000
while True :
    while val < 17000: #tant que val ne dépasse la valeur maximale possible donner en PWM. Cet valeur correspond à un angle de 180°
        val=val+1000 #incrémentation de val
        utime.sleep(1)
        Servo_PWM.duty_u16(val) #Envoit la valeur de val en PWM au Servo
    while val>4000:      #tant que val ne dépasse la valeur minimale possible donner en PWM. Cet valeur correspond à un angle de 0°
        val = val-1000 #décrémentation de val
        utime.sleep(1)
        Servo_PWM.duty_u16(val) #Envoit la valeur de val en PWM au Servo
    