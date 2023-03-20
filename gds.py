import mysql.connector
from tkinter import *

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2206",
  database="boutique"
)

# Création de la fenêtre principale
root = Tk()
root.title("Gestion de stock")

# Fonction pour afficher tous les produits en stock
def afficher_produits():
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM produit")
  produits = mycursor.fetchall()
  for produit in produits:
    print(produit)

# Fonction pour ajouter un produit
def ajouter_produit(nom, description, prix, quantite, categorie):
  mycursor = mydb.cursor()
  sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
  val = (nom, description, prix, quantite, categorie)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "produit ajouté")

# Fonction pour supprimer un produit
def supprimer_produit(id):
  mycursor = mydb.cursor()
  sql = "DELETE FROM produit WHERE id = %s"
  val = (id,)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "produit supprimé")

# Fonction pour modifier un produit
def modifier_produit(id, quantite=None, prix=None):
  mycursor = mydb.cursor()
  sql = "UPDATE produit SET quantite = %s, prix = %s WHERE id = %s"
  val = (quantite, prix, id)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "produit modifié")

# Création des widgets pour ajouter un produit
Label(root, text="Nom").grid(row=0, column=0)
nom_entry = Entry(root)
nom_entry.grid(row=0, column=1)

Label(root, text="Description").grid(row=1, column=0)
description_entry = Entry(root)
description_entry.grid(row=1, column=1)

Label(root, text="Prix").grid(row=2, column=0)
prix_entry = Entry(root)
prix_entry.grid(row=2, column=1)

Label(root, text="Quantité").grid(row=3, column=0)
quantite_entry = Entry(root)
quantite_entry.grid(row=3, column=1)

Label(root, text="Catégorie").grid(row=4, column=0)
categorie_entry = Entry(root)
categorie_entry.grid(row=4, column=1)

Button(root, text="Ajouter produit", command=lambda: ajouter_produit(nom_entry.get(), description_entry.get(), prix_entry.get(), quantite_entry.get(), categorie_entry.get())).grid(row=5, column=1)

# Création des widgets pour supprimer un produit
Label(root, text="ID produit à supprimer").grid(row=6, column=0)
supprimer_entry = Entry(root)
supprimer_entry.grid(row=6, column=1)

Button(root, text="Supprimer produit", command=lambda: supprimer_produit(supprimer_entry.get())).grid(row=7, column=1)

# Création des widgets pour modifier un produit
Label(root, text="ID produit à modifier").grid(row=8, column=0)
modifier_entry = Entry(root)
modifier_entry.grid(row=8, column=1)

Label(root, text="Nouvelle quantité").grid(row=9, column=0)
nouvelle_quantite_entry = Entry(root)
nouvelle_quantite_entry.grid(row=9, column=1)

Label(root, text="Nouveau prix").grid(row=10, column=0)
nouveau_prix_entry = Entry(root)
nouveau_prix_entry.grid(row=10, column=1)

Button(root, text="Modifier produit", command=lambda: modifier_produit(modifier_entry.get(), nouvelle_quantite_entry.get(), nouveau_prix_entry.get())).grid(row=11, column=1)

afficher_produits()

root.mainloop()