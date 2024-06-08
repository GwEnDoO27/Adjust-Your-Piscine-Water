import tkinter as tk
from tkinter import messagebox


def calc_dpd1():
    try:
        user_input = float(dpd1_entry.get())
        print(user_input)
        result = find_dpd1(user_input)
        messagebox.showinfo("Résultat", result)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")


def calc_stab():
    try:
        user_input = float(Stab_entry.get())
        result = find_Stabilisant(user_input)
        messagebox.showinfo("Résultat", result)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")


def calc_dpd3():
    try:
        user_input = float(DpD3_entry.get())
        result = find_Dpd3(user_input)
        messagebox.showinfo("Résultat", result)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")


def calc_pH():
    try:
        user_input = float(DpD3_entry.get())
        result = find_Ph(user_input)
        messagebox.showinfo("Résultat", result)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")


def find_Ph(user_input):
    if user_input < 6.5:
        return "Dpd1 trop bas (trop acide), Réajuster avec du ph+"
    elif user_input >= 6.5 and user_input < 6.9:
        return "Ph un peu bas (trop acide), Réajuster avec du ph+"
    elif user_input >= 6.9 and user_input <= 7.7:
        return "Ph correct"
    elif user_input > 4 and user_input <= 10:
        return "Ph un peu trop haut (trop basique), Réajuster avec du ph -"
    else:
        return "Ph trop Haut, Trop Basique"


def find_Stabilisant(user_input):
    if user_input < 10:
        return "Stabilisant trop bas+"
    elif user_input >= 10 and user_input <= 75:
        return "Stabilisant correct"
    elif user_input > 75 and user_input <= 125:
        return "Stabilisant trop haut\nConseil : Vidage partiel du bassin ou traitemetn avec du chlore stabilisé"
    else:
        return "Stabilisant trop haut\nVidage partiel du bassin avec augmentation en apport d'eau neuve"


def find_dpd1(user_input):
    if user_input < 0.5:
        return "Dpd1 trop bas"
    elif 0.5 <= user_input < 2:
        return "Dpd1 un peu bas, Augmenter l'injection de désinfectant"
    elif 2 <= user_input < 4:
        return "Dpd1 correct"
    elif 4 <= user_input <= 10:
        return "Dpd1 un peu haut, Diminuer l'injection et apporter de l'eau neuve"
    else:
        return "Dpd1 trop haut"


def find_Dpd3(number):
    return number / 2


# Créer la fenêtre principale
root = tk.Tk()
root.title("Caculateur")
root.geometry("400x550")

# Créer une étiquette
label = tk.Label(root, text="Bienvenue dans le calculateur !")
label.pack(pady=10)

# Champ d'entrée et bouton pour le Dpd1
dpd1_label = tk.Label(root, text="Entrer le dpd1 :")
dpd1_label.pack(pady=5)
dpd1_entry = tk.Entry(root, width=40)
dpd1_entry.pack(pady=5)
dpd1_button = tk.Button(root, text="Submit", command=calc_dpd1)
dpd1_button.pack(pady=10)

# Champ d'entrée et bouton pour le Stabilisant
Stab_label = tk.Label(root, text="Entrez le Stabilisant :")
Stab_label.pack(pady=5)
Stab_entry = tk.Entry(root, width=40)
Stab_entry.pack(pady=5)
Stab_button = tk.Button(root, text="Submit", command=calc_stab)
Stab_button.pack(pady=10)

# Champ d'entrée et bouton pour le Dpd3
DpD3_label = tk.Label(root, text="Entrez DpD3 :")
DpD3_label.pack(pady=5)
DpD3_entry = tk.Entry(root, width=40)
DpD3_entry.pack(pady=5)
DpD3_button = tk.Button(root, text="Submit", command=calc_dpd3)
DpD3_button.pack(pady=10)

# Champ d'entrée et bouton pour le pH
ph_label = tk.Label(root, text="Entrez le pH :")
ph_label.pack(pady=5)
ph_entry = tk.Entry(root, width=40)
ph_entry.pack(pady=5)
ph_button = tk.Button(root, text="Submit", command=calc_pH)
ph_button.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
