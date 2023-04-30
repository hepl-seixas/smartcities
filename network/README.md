# 0) Introduction
Cette partie va présenter comment programmer un pico afin d'accéder à internet. Ce qui permettre d'accéder à la date et l'heure mais aussi à un API (par exemple, OPEN WEATHER MAP). Pour simplifier le pocéder de connexion, on va créer un fichier (nommée secrets) qui contiendra un dictionnaire avec tous les données nécéssaires aux différents code : SSID, mot de passe, clé API, ...
```
my_secrets = {
    "ssid" : "Proximus-Home-2198",
    "WiFi_pass" : "wpuk4z3yyhwp7",
    "OWM_API_key" : "3a3ace8108cb08fc1b48cc858ffd2d23",
    # My location :
    "lat" : "50.632557", #coordonnées de Liège
    "lon" : "5.579666"
}
```
Remarque : cette partie a été réalisé chez moi donc le SSID et le mot de passe sont ceux de chez moi.
# 1) Connexion Wifi
Cette partie va s'intéresser à la manière de réaliser une connexion wifi à l'aide de la librairie network
## 1.1 ) Description des méthodes
- network.WLAN (network.STA_IF) : créer un objet WLAN
- wlan.active(True) : active l'objet WLAN
- wlan.connect (SSID, mot_de_passe) : connecte l'objet WLAN à un réseau wifi du nom de SSID
- wlan.disconnect() : déconnecte l'objet WLAN.
## 1.2) Programme
```
import network
from secrets import *
import utime

wlan = network.WLAN(network.STA_IF) # Créer un Objet WLAN
wlan.active(True) #active l'objet WLAN
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"]) # connection du WLAN au réseau wifi indiqué dans le dictionnaire contenu dans le fichier secrets

wlan.disconnect()  #deconnexion du RPI
```
Ce programme réalise seulement une connexion wifi mais il n'y a aucune véréfication de si la connexion s'est bien réalisé

# 2) Affichage de la date et de l'heure sur le LCD grâce à NTP
Cette partie va s'intéresser à la façon de se connecter sur le service NTP afin d'obtenir la date et l'heure.
## 2.1 ) Description des méthodes
- socket.getaddrinfo(host, port) : retourne des infos sur l'hôte (adresse IP, ...)
- socket.socket(socket.AF_INET, socket.SOCK_DGRAM) : créer un socket se basant sur le protocole UDP/IP
- socket.sendto(NTP_QUERY, addr) : envoie un message de NTP_QUERY bytes à l'adresse ADR permettant d'initialiser la communication
- socket.recv(48) : reçois un message de 48 bytes
- s.close() : ferme la connection du socket
- struct.unpack("!I", msg[40:44]) : permet d'extraire certaines informations

## 2.2) Programme
```
import network, socket
import struct
from secrets import *
import utime
from lcd1602 import LCD1602
from machine import I2C,Pin,ADC,PWM

# connexion au wifi

wlan = network.WLAN(network.STA_IF) # Créer un Objet WLAN
wlan.active(True) #active l'objet WLAN
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"]) # connection du WLAN au réseau wifi indiqué dans le dictionnaire contenu dans le fichier secrets

def get_time(offset=7200, delta=2208988800, host="pool.ntp.org"):  # offset représente le décallage horaire en seconde (ici on est à UTC + 2 )
                                                                   # delta représente le nombre de seconde écoulé depuis le 01/01/1900
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B # version 3 mode 3
    addr = socket.getaddrinfo(host, 123)[0][-1] # permet d'obtenir l'adresse IP de l'hôte # 123 is the port number for NTP
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # création d'un socket
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr) # envoie d'un ping contenant quelques informations au server afin d'initialiser la communication
        
        msg = s.recv(48) # reçois le message (de 48 byte)
    finally:
        s.close() # ferme la connection
        
    val = struct.unpack("!I", msg[40:44])[0] # extrait plusieurs données du server (les données 40 à 44 contiennent le temps)
    t = val - delta # convertit le temps venant de NTP en le véritable temps  
    tm = utime.gmtime(t+offset) # rajout du décalage horaire 
    return tm  # retourne : année, mois, jour, heur, minute, seconde, ...

t_now=get_time() # Utilisation de la fonction

# ferme la connection au wifi
wlan.disconnect()

# configuration du LCD

i2c = I2C(1,scl = Pin(7), sda = Pin(6),freq = 400000) #programmation de l'interface I2C utilisé
d = LCD1602 (i2c,2,16) #création de l'objet LCD1602
d.display() #active le LCD

d.print("Time is: {:2d}:{:02d}:{:02d}".format(t_now[3],t_now[4],t_now[5])) #affiche l'heure (heure minue et seconde) espacé par des ":"") #affichage de Hello world
d.setCursor(0,1) #mise du curseur à la position 0,1
d.print ("Date is: {:2d}/{:02d}".format(t_now[2],t_now[1])) #affichage de la date (il n'y a pas suffisament de place sur le LCD pour afficher l'année)

```
![image](https://user-images.githubusercontent.com/124899641/235364779-9e868c65-d3db-46c4-895c-b38891763ce5.png)
Ce code donne bien la date et l'heure. Malheureusement, il n'est pas possible d'afficher toute la date car le LCD ne permet d'afficher que 2x16 carctères.

# 3) Affichage de la météo à l'ade de Open weather map
Cette partie va présenter la manière de réaliser une connexion entre le RPI et open weather map
## 3.1) Description des méthodes
- requests.get(URL) : envoie une requête de type get (on demande des données) à une URL donnée
- request.json() : formatage de la requête en format json
## 3.2) Programme

```
import urequests as requests
import network
from secrets import *
import utime
# Réalisation d'une connexion wifi
wlan = network.WLAN(network.STA_IF) # Créer un Objet WLAN
wlan.active(True) #active l'objet WLAN
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"]) # connection du WLAN au réseau wifi indiqué dans le dictionnaire contenu dans le fichier secrets
# Now we can use the connection to access Internet.


URL = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (my_secrets["lat"], my_secrets["lon"],my_secrets["OWM_API_key"]) # enregistrement de l'URL avec les paramètres intéressant (latitude, longitude, ...)
r = requests.get(URL) #requête get vers l'API
print (r.json()) #affichage et mise en format json des données météos 

# Close connection
wlan.disconnect()  #deconnexion du RPI
```
![image](https://user-images.githubusercontent.com/124899641/235354207-8023a374-86c4-4c12-aec7-cad9c718c265.png)

Il est évidemment possible de filtrer les données reçu, La requête get a donné un dictionnaire donc il est possible de le traiter comme il nous plait

