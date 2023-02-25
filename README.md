# smartcities
Ce github introduit les différentes notions nécessaire afin de travailler avec le Grove starter kit pico. Afin de se faire, il faut se familiariser avec : le micropython, l'IDE Thonny et le Raspberry Pi Pico.

1) micropython

  Le python est un langage de programmation très utilisé pour les appareils puissants ayant suffisament de mémoire. C'est pour cela que le micropython est né.
  
  Il s'agit simplement du langage python très optimisé. 
  
  Afin de pouvoir l'utilisé sur le Raspberry Pi Pico, il faut installer micropython sur le Raspberry Pi Pico. Pour se faire, il suffit de maintenir le button du RPI enfoncé avant et après avoir connecté le RPI sur le PC. Ceci ouvrire un dossier contenant la mémoire du RPI, il suffit juse de déposer micropython dans ce dossier.
  
3) Thonny
  Thonny est un IDE simple d'utilisation permettant le codage du python et du micropython. Afin de l'utiliser, il faut :
    a) le télécharger via ce lien : https://thonny.org/
    b) changer l'interpreteur par : MicroPython (Raspberry Pi Pico).
    ![image](https://user-images.githubusercontent.com/124899641/221367883-a4a8a8b0-ef89-4435-8673-d2fd268365fc.png)

  L'interface de thonny contient :
  
    1) une barre d'outils permettant notammenet de démarrer/arrêter un script
    
    2) une zone de texte permettant d'écrire le script
    
    3) Un shell dans lequel le script sera exécuté
    
    4) Un interpréteur permettant de choisir notamment si le programme est codé en python ou en micro python
 
3) Raspberry Pi Pico
  C'est un microcontrolleur designé par Raspberry Pi. Il possède 26 pins GPIO multifonction incluant : 2 SPI, 2 I2C, 2 UART, 12 ADC de 12 bits et 16 canaux PWM
  ![image](https://user-images.githubusercontent.com/124899641/221366412-c38ba80d-ed7f-4ccb-8af2-fbd214e8f118.png)
  
  En plus de ce Raspberry Pi Pico, le grove starter kit pico fournit :
  
    - un shield rajoutant : 2 I2C, 3 ADC, 2 UART, 3 ports digitaux et 1 SPI.
    
    - plusieurs modules : capteur de lumière, detecteur de son, detecteur de mouvement, detecteur de température et d'humidité, potentiometre, boutton indépendant, module de LED, module de LED RGB, buzzer passif, relay, écran LCD, servo moteur, un driver motor.
    

Lien vers les différents sous-répertoire :
[GPIO](GPIO)
[AD-PWM](AD-PWM)
[LCD](LCD)
[LED_neo](LED_neo)
[sensors](sensors)
[network](network)
