from flask import Flask, render_template,request  # Impotation de Flask, render_template : Cette fonction permet de rendre (ou afficher) des templates HTML. Elle prend en entrée le nom du fichier template et les variables optionnelles à passer au template. request : Cet objet contient toutes les données relatives à la requête HTTP entrante. Il permet d’accéder aux données de formulaire soumises par l’utilisateur.
import qrcode # Impotation du qrcode
from io import BytesIO # Importation de BytesIO de la bibliothèque io. BytesIO est utilisé pour gérer les données binaires en mémoire comme s’il s’agissait d’un fichier.
from base64 import b64encode # Importation de la fonction b64encode de la bibliothèque base64. Elle permet de convertir des données binaires en chaîne de caractères encodée en base64, utile pour l’affichage d’images directement dans le code HTML.
app = Flask(__name__) # Création d’une instance de l’application Flask. Le paramètre __name__ est utilisé pour dire à Flask où chercher les fichiers et ressources de l’application.

@app.route('/') # Décorateur Flask qui lie l’URL / à la fonction home. Cela signifie que lorsque l’utilisateur accède à la racine du site (par exemple, http://localhost:5000/), la fonction home est appelée.
def home():
    return render_template ('index.html') # Cette ligne rend le template HTML index.html. Elle envoie le fichier HTML index.html au navigateur de l’utilisateur pour affichage.


@app.route('/', methods=['POST']) # Décorateur Flask qui lie l’URL / à la fonction generateQR, mais seulement pour les requêtes HTTP POST. Cela signifie que lorsque l’utilisateur soumet un formulaire POST à la racine du site, la fonction generateQR est appelée.
def generateQR(): # Crée un objet BytesIO en mémoire pour stocker temporairement l’image du QR code.
    memory = BytesIO() # Crée un objet BytesIO en mémoire pour stocker temporairement l’image du QR code.
    data = request.form.get('link') # Récupère les données du formulaire soumises par l’utilisateur sous le champ link. Cette donnée est l’URL ou le texte que l’utilisateur veut convertir en QR code.
    img = qrcode.make(data) # Utilise la bibliothèque qrcode pour créer un QR code à partir des données soumises.
    img.save(memory) # Sauvegarde l’image du QR code dans l’objet BytesIO en mémoire.
    memory.seek(0) # Remet le curseur du BytesIO au début, prêt à lire les données.
    
    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii') # Encode les données de l’image en base64 pour pouvoir les inclure directement dans le code HTML comme une image inline.       
    return render_template ('index.html', data=base64_img) # Rend à nouveau le template index.html, mais cette fois en passant base64_img comme variable. Cela permet au template d’afficher l’image du QR code.
    
if __name__ == '__main__': # Cette condition vérifie si le script est exécuté directement (et non importé comme module). Si c’est le cas, elle lance l’application Flask.
    app.run(debug=True) # Démarre le serveur web Flask en mode debug. Le mode debug est utile pour le développement car il recharge automatiquement l’application à chaque changement de code et affiche des messages d’erreur détaillés.
