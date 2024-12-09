from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from tkinter import font
# from page1 import *
import db_client_mongodb
class CLientClassMongo:
    def afficher_interface2(self):
        #TODO insitialisation de la page
        self.page2 = Tk()
        self.page2.config(background="#006666")
        #TODO font
        self.p2_nouvelle_police = font.Font(family="Calibri", size=14, weight="bold")
        self.p2_font_champ = font.Font(family="Calibri", size=12, weight="bold",slant="italic")
        self.p2_font_button = font.Font(family="Calibri", size=13, weight="bold",slant="italic")
        self.p2_font_button_chercher = font.Font(family="Calibri", size=12, weight="bold",slant="italic")
        self.p2_font_button_table_1_2 = font.Font(family="Calibri", size=10, weight="bold",slant="italic")

        #TODO geometry
        self.page2.geometry("1200x600")
        #TODO title
        self.page2.title("CLIENT")
        #TODO self.page2 not resizable
        self.page2.resizable(False,False)

        #! CHAMP DE SAISIE
        self.id_client_label = Label(self.page2,text="ID",background="#006666",fg="#fff",font=self.p2_font_champ)
        self.id_client_entrer = Entry(self.page2,border=1,width=20)
        self.nom_client_label = Label(self.page2,text="NOM",background="#006666",fg="#fff",font=self.p2_font_champ)
        self.nom_client_entrer = Entry(self.page2,border=1,width=20)
        self.prenom_client_label = Label(self.page2,text="PRENOM",background="#006666",fg="#fff",font=self.p2_font_champ)
        self.prenom_client_entrer = Entry(self.page2,border=1,width=20)
        self.tel_client_label = Label(self.page2,text="TELEPHONE",background="#006666",fg="#fff",font=self.p2_font_champ)
        self.tel_client_entrer = Entry(self.page2,border=1,width=20)
        self.adrs_client_label = Label(self.page2,text="ADRESS DE LAIVRAISON",background="#006666",fg="#fff",font=self.p2_font_champ)
        self.adrs_client_entrer = Entry(self.page2,border=1,width=35)
        self.p2_btn_vider = Button(self.page2,text="effacer",padx= 10,pady=1,command=self.clear_All_input,background="#ff073a", fg="#000", font=self.p2_font_button,cursor='hand2')

        self.p2_b1 = Button(self.page2,text="ajouter",padx= 23,pady=1,command=self.ajouter, fg="#000", font=self.p2_font_button,cursor='hand2')
        self.p2_b1.place(x=25, y=25)
        self.p2_b2 = Button(self.page2,text="modifier",padx= 20,pady=1,command=self.modifier, fg="#000", font=self.p2_font_button,cursor='hand2')
        self.p2_b2.place(x=25, y=80)
        self.p2_b3 = Button(self.page2,text="suprimmer",padx= 10,pady=1,command=self.suprimmer, fg="#000", font=self.p2_font_button,cursor='hand2')
        self.p2_b3.place(x=25, y=135)
        self.p3_b3_prime = Button(self.page2,text="afficher tous",padx= 6,pady=1,command=self.remplir_tableau, fg="#000", font=self.p2_font_button,cursor='hand2')
        self.p3_b3_prime.place(x=25, y=190)
        self.adrs_client_label = Label(self.page2,text="ADRESS DE LAIVRAISON",background="#006666",fg="#fff",font=self.p2_font_champ)
        self.adrs_client_entrer = Entry(self.page2,border=1,width=35)

        self.chercher_email_client_entrer = Entry(self.page2,border=1,width=25)
        self.chercher_email_client_entrer.place(x=180 ,y=25)
        self.p2_b4 = Button(self.page2,text="chercher par email",padx= 10,pady=1,command=self.chercher_par_email, fg="#000", font=self.p2_font_button_chercher,highlightbackground="red",cursor='hand2')
        self.p2_b4.place(x=180, y=50)
        self.chercher_nom_client_entrer = Entry(self.page2,border=1,width=25)
        self.chercher_nom_client_entrer.place(x=180 ,y=120)
        self.p2_b4_chercher_nom = Button(self.page2,text="chercher par nom",padx= 10,pady=1,command=self.chercher_par_nom, fg="#000", font=self.p2_font_button_chercher,highlightbackground="red",cursor='hand2')
        self.p2_b4_chercher_nom.place(x=180, y=145)
        self.table2()
        self.p2_table2.bind('<ButtonRelease>',self.selected_row) #la fonction sans parentese
        self.hover_button()
        self.show_input()
        self.remplir_tableau()
        self.page2.mainloop()

    def show_input(self):
        self.id_client_label.place(x=550,y=25)
        self.id_client_entrer.place(x=600,y=30)
        self.prenom_client_label.place(x=530,y=60)
        self.prenom_client_entrer.place(x=600,y=65)
        self.nom_client_label.place(x=800,y=25)
        self.nom_client_entrer.place(x=850,y=30)
        self.tel_client_label.place(x=760,y=60)
        self.tel_client_entrer.place(x=850,y=65)
        self.adrs_client_label.place(x=490,y=100)
        self.adrs_client_entrer.place(x=670,y=105)
        self.p2_btn_vider.place(x=730, y=150)

    def ajouter(self):
        self.show_input()
        id = self.id_client_entrer.get()
        nom = self.nom_client_entrer.get()
        email = self.prenom_client_entrer.get()
        mdp = self.tel_client_entrer.get()
        adress = self.adrs_client_entrer.get()
        # if id == '' or nom == '' or email == '' or mdp == '' or adress == '':
        #     tkinter.messagebox.showerror('',"CHAMP VIDE")
        # elif db_client.chercher_client(id):
        #     tkinter.messagebox.showerror('',"CLIENT DEJA EXIST")
        # else:
        #     db_client.ajouter(id=id,nom=nom,email=email,mdp=mdp,adress=adress)
        #     self.remplir_tableau()
        #     tkinter.messagebox.showinfo('',"CLIENT AJOUTE AVEC SUCCES")
        #     self.clear_All_input()


    def remplir_tableau(self):
        #? Récupération de tous les clients depuis MongoDB
        all_client = db_client_mongodb.get_all_client_mongo()
        #? Réinitialisation des lignes existantes
        self.p2_table2.delete(*self.p2_table2.get_children())
        #? Ajout des données dans le tableau
        for client in all_client:
            self.p2_table2.insert('', 'end', values=(
                client['_id'], 
                client['nom'], 
                client['prenom'], 
                client['telephone'], 
                client['adress']
            ))

    def selected_row(self,event):
        self.show_input()
        self.clear_All_input()
        client_selectionne = self.p2_table2.focus()
        if client_selectionne:
            info_client = self.p2_table2.item(client_selectionne)['values']
            self.id_client_entrer.insert(0,info_client[0])
            self.nom_client_entrer.insert(0,info_client[1])
            self.prenom_client_entrer.insert(0,info_client[2])
            self.tel_client_entrer.insert(0,info_client[3])
            self.adrs_client_entrer.insert(0,info_client[4])

    def modifier(self):
        client_selectionne = self.p2_table2.focus()  # Récupérer le client sélectionné dans la table
        if client_selectionne:  # Vérifier si un client est sélectionné
            id = self.id_client_entrer.get()  # Récupérer l'id du client
            nv_nom = self.nom_client_entrer.get()  # Récupérer le nouveau nom
            nv_prenom = self.prenom_client_entrer.get()  # Récupérer le nouveau prénom
            nv_telephone = self.tel_client_entrer.get()  # Récupérer le nouveau téléphone
            nv_adress = self.adrs_client_entrer.get()  # Récupérer la nouvelle adresse
            
            # Appeler la fonction modifier pour mettre à jour les données dans la base de données MongoDB
            db_client_mongodb.modifier(nv_nom=nv_nom, nv_prenom=nv_prenom, nv_telephone=nv_telephone, nv_adress=nv_adress, id=int(id))
            
            # Rafraîchir le tableau pour afficher les nouvelles données
            self.remplir_tableau()
            
            # Afficher un message de succès
            tkinter.messagebox.showinfo('', "CLIENT MODIFIÉ AVEC SUCCÈS")
            
            # Effacer les champs de saisie
            self.clear_All_input()
        else:
            tkinter.messagebox.showerror('', "SÉLECTIONNER LE CLIENT D'ABORD")

    def suprimmer(self):
        client_selectionne = self.p2_table2.focus()
        # if client_selectionne:
        #     id = self.id_client_entrer.get()
        #     db_client.suprimmer_client(id=id)
        #     self.remplir_tableau()
        #     tkinter.messagebox.showinfo('',"CLIENT SUPRIMMER AVEC SUCCES")
        #     self.clear_All_input()
        # else:
        #     tkinter.messagebox.showerror('',"SELECTIONNER LE CLIENT D'BBORD")

    def chercher_par_email(self):
        self.remplir_tableau()
        # email = self.chercher_email_client_entrer.get()
        # results = db_client.chercher_client_email(email=email)
        # self.p2_table2.delete(*self.p2_table2.get_children())
        # for result in results:
        #     self.p2_table2.insert('',END,values=result)
        # self.chercher_email_client_entrer.delete(0,END)

    def chercher_par_nom(self):
        self.remplir_tableau()
        # nom = self.chercher_nom_client_entrer.get()
        # clients = db_client.chercher_client_nom(nom)
        # self.p2_table2.delete(*self.p2_table2.get_children())
        # for client in clients:
        #     self.p2_table2.insert('',END,values=client)
        # self.chercher_nom_client_entrer.delete(0,END)

    def clear_All_input(self):
        self.id_client_entrer.delete(0, END)  # Deletes all characters
        self.nom_client_entrer.delete(0, END)
        self.prenom_client_entrer.delete(0, END)
        self.tel_client_entrer.delete(0, END)
        self.adrs_client_entrer.delete(0, END)

    def on_enter1(self,e):
        self.p2_b1['background'] = '#006666'  # Change la couleur au survol
        self.p2_b1['fg'] = '#fff'
        self.p2_b1['font'] = self.p2_font_button
    def on_enter2(self,e):
        self.p2_b2['background'] = '#006666'
        self.p2_b2['fg'] = '#fff'
        self.p2_b2['font'] = self.p2_font_button
    def on_enter3(self,e):
        self.p2_b3['background'] = '#006666'
        self.p2_b3['fg'] = '#fff'
        self.p2_b3['font'] = self.p2_font_button

    def on_leave1(self,e):
        self.p2_b1['background'] = '#fff'  # Revient à la couleur normale
        self.p2_b1['fg'] = '#000'
        self.p2_b1['font'] = self.p2_font_button
    def on_leave2(self,e):
        self.p2_b2['background'] = '#fff'
        self.p2_b2['fg'] = '#000'
        self.p2_b2['font'] = self.p2_font_button
    def on_leave3(self,e):
        self.p2_b3['background'] = '#fff'
        self.p2_b3['fg'] = '#000'
        self.p2_b3['font'] = self.p2_font_button

    def hover_button(self):
        #apllique les function de hover
        self.p2_b1.bind("<Enter>", self.on_enter1)
        self.p2_b1.bind("<Leave>", self.on_leave1)
        self.p2_b2.bind("<Enter>", self.on_enter2)
        self.p2_b2.bind("<Leave>", self.on_leave2)
        self.p2_b3.bind("<Enter>", self.on_enter3)
        self.p2_b3.bind("<Leave>", self.on_leave3)

    def table2(self):
        # Création de la table Treeview
        self.p2_table2 = ttk.Treeview(self.page2, height=15)
        self.p2_table2['columns'] = ('ID', 'NOM','PRENOM', 'TEL', 'ADRESS')

        # Configuration des colonnes
        self.p2_table2.column('#0', stretch=tk.NO, width=0)
        self.p2_table2.column('ID', anchor=tk.CENTER, width=100)
        self.p2_table2.column('NOM', anchor=tk.CENTER, width=250)
        self.p2_table2.column('PRENOM', anchor=tk.CENTER, width=250)
        self.p2_table2.column('TEL', anchor=tk.CENTER, width=250)
        self.p2_table2.column('ADRESS', anchor=tk.CENTER, width=300)

        # Définition des entêtes
        self.p2_table2.heading('ID', text='ID')
        self.p2_table2.heading('NOM', text='NOM')
        self.p2_table2.heading('PRENOM', text='PRENOM')
        self.p2_table2.heading('TEL', text='TEL')
        self.p2_table2.heading('ADRESS', text='ADRESS')

        # Positionnement de la table
        self.p2_table2.place(x=25, y=240)
        # self.p2_table2.place(x=10, y=240, relwidth=0.95, relheight=0.7)

p1 = CLientClassMongo()
p1.afficher_interface2()