import qrcode
import json

# Informations à inclure dans le QR Code
data = {
    "url": "https://anime-sama.fr/catalogue/shingeki-no-kyojin/",
    "geo": {
        "latitude": 37.7749,
        "longitude": -122.4194
    },
    "wifi": {
        "ssid": "YourNetworkSSID",
        "auth_type": "WPA",  # Peut être WPA, WEP ou nopass
        "password": "YourNetworkPassword"
    }
}

# Convertir les informations en format JSON
json_data = json.dumps(data)

# Créer une instance de QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajouter les données JSON
qr.add_data(json_data)
qr.make(fit=True)

# Créer une image du QRCode
img = qr.make_image(fill='black', back_color='white')

# Sauvegarder l'image dans un fichier
img.save("qrcode.png")
