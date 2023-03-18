from machine import Pin, PWM
import utime

buzzer = PWM(Pin(20))       #Utilisation de la pin 20 comme pin PWM
def DO (vol, time):         #création des différentes notes joué dans la chanson sous forme de fonction prennant en paramètre leur volume et le temps de jeu
    buzzer.freq (1046)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def RE (vol, time):
    buzzer.freq (1175)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def MI (vol, time):
    buzzer.freq (1318)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def FA (vol, time):
    buzzer.freq (1397)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def SOL (vol, time):
    buzzer.freq (1568)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def LA (vol, time):
    buzzer.freq (1760)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def SI_bemol (vol, time):
    buzzer.freq (1864)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def DO_2 (vol, time):
    buzzer.freq (2043)
    buzzer.duty_u16(vol)
    utime.sleep(time)
def N():
    buzzer.duty_u16(0) #volume de 0 afin que la dernière note éteigne le son du buzzer
    utime.sleep(0.35)
DO(1000, 0.35)           #appel des différentes fonctions dans l'ordre afin de créer la musique 
DO(1000, 0.35)
RE(1000, 0.35)
DO(1000, 0.35)
FA(1000, 0.35)
MI(1000, 0.35)
DO(1000, 0.35)
DO(1000, 0.35)
RE(1000, 0.35)
DO(1000, 0.35)
SOL(1000, 0.35)
FA(1000, 0.35)
DO(1000, 0.35)
DO(1000, 0.35)
DO_2(1000, 0.35)
LA(1000, 0.35)
FA(1000, 0.35)
MI(1000, 0.35)
RE(1000, 0.35)
SI_bemol(1000, 0.35)
SI_bemol(1000, 0.35)
LA(1000, 0.35)
FA(1000, 0.35)
SOL(1000, 0.35)
FA(1000, 0.35)
N()