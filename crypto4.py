import tkinter as tk
from tkinter import messagebox
import string

# Fenêtre principale
root = tk.Tk()
root.title("Text ↔ Numeric Converter")
root.geometry("800x750")
root.configure(bg="#f0f4f7")

# Dictionnaires
char_to_num = {}
num_to_char = {}

# Lettres + caractères spéciaux
default_letters = list(string.ascii_lowercase) + [' ', ',', "'", '.', 'é', 'è', 'à', 'ç']

# Mapping par défaut
default_numbers = [f"{i+1:03}" for i in range(26)] + ['000','027','028','029','030','031','032','033']

# Fonction pour définir le mapping
def set_mapping():
    numbers = entry_numbers.get().split(",")
    if len(default_letters) != len(numbers):
        messagebox.showerror("Erreur", f"Le nombre de nombres doit être égal à {len(default_letters)}.")
        return
    global char_to_num, num_to_char
    char_to_num = {}
    num_to_char = {}
    for l, n in zip(default_letters, numbers):
        n = n.strip()
        char_to_num[l] = n
        num_to_char[n] = l
    messagebox.showinfo("Succès", "Mappings enregistrés !")

# Texte → chiffres
def text_to_number():
    text = entry_text.get().lower()
    result = []
    for char in text:
        result.append(char_to_num.get(char,"?"))
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, " ".join(result))

# Chiffres → texte
def number_to_text():
    numbers = entry_text.get().split()
    result = []
    for num in numbers:
        result.append(num_to_char.get(num,"?"))
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "".join(result))

# Copier résultat
def copy_result():
    root.clipboard_clear()
    root.clipboard_append(text_result.get("1.0", tk.END).strip())
    messagebox.showinfo("Copié", "Le résultat a été copié dans le presse-papiers.")

# Coller résultat dans texte
def paste_result():
    entry_text.delete(0, tk.END)
    entry_text.insert(0, text_result.get("1.0", tk.END).strip())

# Styles
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
btn_font = ("Helvetica", 12, "bold")

# Widgets
tk.Label(root, text="Chiffres correspondants pour chaque lettre et caractère spécial (séparés par ,) :", 
         font=label_font, bg="#f0f4f7").pack(pady=5)

entry_numbers = tk.Entry(root, width=120, font=entry_font, bg="#e6f2ff")
entry_numbers.pack()
entry_numbers.insert(0, ",".join(default_numbers))

btn_set_mapping = tk.Button(root, text="Enregistrer Mappings", font=btn_font, bg="#4CAF50", fg="white",
                            activebackground="#45a049", command=set_mapping)
btn_set_mapping.pack(pady=10)

tk.Label(root, text="Entrez votre texte ou chiffres :", font=label_font, bg="#f0f4f7").pack(pady=5)
entry_text = tk.Entry(root, width=120, font=entry_font, bg="#fff2cc")
entry_text.pack()

btn_text_to_num = tk.Button(root, text="Texte → Chiffres", font=btn_font, bg="#2196F3", fg="white",
                            activebackground="#1976D2", command=text_to_number)
btn_text_to_num.pack(pady=5)

btn_num_to_text = tk.Button(root, text="Chiffres → Texte", font=btn_font, bg="#FF9800", fg="white",
                            activebackground="#e68a00", command=number_to_text)
btn_num_to_text.pack(pady=5)

# Boutons copier/coller
btn_copy = tk.Button(root, text="Copier le résultat", font=btn_font, bg="#9C27B0", fg="white",
                     activebackground="#7B1FA2", command=copy_result)
btn_copy.pack(pady=5)

btn_paste = tk.Button(root, text="Coller le résultat dans le texte", font=btn_font, bg="#607D8B", fg="white",
                      activebackground="#455A64", command=paste_result)
btn_paste.pack(pady=5)

tk.Label(root, text="Résultat :", font=label_font, bg="#f0f4f7").pack(pady=5)
text_result = tk.Text(root, width=90, height=15, font=("Courier", 14), bg="#fefbd8")
text_result.pack(pady=10)

root.mainloop()
