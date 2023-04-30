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


## 2.2) Programme

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

