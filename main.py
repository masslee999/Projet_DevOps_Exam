
import qrcode

# Lien vers le site web
url = "https://anime-sama.fr/catalogue/shingeki-no-kyojin/"

# Créer une instance de QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajouter le lien
qr.add_data(url)
qr.make(fit=True)

# Créer une image du QRCode
img = qr.make_image(fill='black', back_color='white')

# Sauvegarder l'image dans un fichier
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")