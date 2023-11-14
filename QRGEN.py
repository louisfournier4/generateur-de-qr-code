import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# Couleurs personnalisées
background_color = "#37474F"  # Couleur de l'arrière-plan
text_color = "white"  # Couleur du texte
button_bg = "#0277BD"  # Couleur de fond des boutons
button_fg = "white"  # Couleur du texte des boutons

# Police personnalisée
font = ("Arial", 18)

# Fonction pour générer un QR code
def generate_qr_code():
    data = link_entry.get()
    filename = "qrcode.png"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    qr_code_image = Image.open("qrcode.png")
    qr_code_image = ImageTk.PhotoImage(qr_code_image)
    qr_code_label.config(image=qr_code_image)
    qr_code_label.image = qr_code_image
    status_label.config(text="QR code généré avec succès!")

# Fonction pour enregistrer un QR code
def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Fichiers PNG", "*.png")])
    if file_path:
        generate_qr_code()
        qr_code_image = Image.open("qrcode.png")
        qr_code_image.save(file_path)
        status_label.config(text="QR code sauvegardé avec succès!")

# Fonction pour afficher la page du générateur
def show_generator():
    homepage_frame.pack_forget()  # Masquer la page d'accueil
    generator_frame.pack(fill="both", expand=True)  # Afficher la page du générateur et étirer pour remplir
    window.update()  # Met à jour la fenêtre pour réorganiser correctement les widgets

# Fonction pour afficher la page d'accueil
def show_homepage():
    generator_frame.pack_forget()  # Masquer la page du générateur
    homepage_frame.pack(fill="both", expand=True)  # Afficher la page d'accueil et étirer pour remplir
    window.update()  # Met à jour la fenêtre pour réorganiser correctement les widgets

# Fonction pour gérer la fermeture de la fenêtre
def on_closing():
    window.destroy()

window = tk.Tk()
window.title("Générateur de QR Code")
window.geometry("800x600")  # Réglez la taille de la fenêtre à 800x600 pixels

# Ajoutez un gestionnaire d'événements pour intercepter la fermeture de la fenêtre
window.protocol("WM_DELETE_WINDOW", on_closing)

# Page d'accueil
homepage_frame = tk.Frame(window, bg=background_color)
homepage_frame.pack(fill="both", expand=True)
homepage_label = tk.Label(homepage_frame, text="Bienvenue sur le générateur de QR code!", font=font, bg=background_color, fg=text_color)
homepage_label.pack(pady=20)

# Centrez votre nom et la déclaration de droits en bas de la page d'accueil
creator_label = tk.Label(homepage_frame, text="Réalisé par Louis Fournier. Tous les droits sont réservés.", font=font, bg=background_color, fg=text_color)
creator_label.pack(side="bottom")

show_generator_button = tk.Button(homepage_frame, text="Générer QR Code", command=show_generator, font=font, bg=button_bg, fg=button_fg)
show_generator_button.pack()

# Page du générateur
generator_frame = tk.Frame(window, bg=background_color)
link_label = tk.Label(generator_frame, text="Entrez le lien:", font=font, bg=background_color, fg=text_color)
link_label.pack()

# Centrez votre nom et la déclaration de droits en bas de la page du générateur
creator_label_generator = tk.Label(generator_frame, text="Réalisé par Louis Fournier. Tous les droits sont réservés.", font=font, bg=background_color, fg=text_color)
creator_label_generator.pack(side="bottom")

link_entry = tk.Entry(generator_frame, font=font)
link_entry.pack()
generate_button = tk.Button(generator_frame, text="Générer QR Code", command=generate_qr_code, font=font, bg=button_bg, fg=button_fg)
generate_button.pack()
save_button = tk.Button(generator_frame, text="Enregistrer QR Code", command=save_qr_code, font=font, bg=button_bg, fg=button_fg)
save_button.pack()
status_label = tk.Label(generator_frame, text="", font=font, bg=background_color, fg=text_color)
status_label.pack()
qr_code_label = tk.Label(generator_frame)
qr_code_label.pack()

# Masquer la page du générateur au démarrage
generator_frame.pack_forget()

window.mainloop()
