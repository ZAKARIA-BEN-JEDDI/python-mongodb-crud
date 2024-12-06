import sqlite3

class Produit_sql:

    def creer_db_produit(self):
        self.connexion = sqlite3.connect('magasin.db')
        self.cursor = self.connexion.cursor()

        #! unique AUTOINCREMENT pour le ID
        self.cursor.execute(''' 
            CREATE TABLE IF NOT IXISTS produit(
                id_produit int(10) not null primary key,self.
                nom_produit varchar(10) not null,
                prix int(20) not null,
                quantite int(20) not null,
                description varchar(20) not null
            )
        ''')
        self.connexion.commit()
        self.connexion.close()

    def get_all_produit(self):
        self.connexion = sqlite3.connect('magasin.db')
        self.cursor = self.connexion.cursor()
        self.cursor.execute('SELECT * FROM produit')
        self.produit = self.cursor.fetchall()
        self.connexion.close()
        return self.produit

    def ajouter_produit(self,id,nom,prix,quantite,description):
        self.connexion = sqlite3.connect('magasin.db')
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''
            INSERT INTO produit (id_produit,nom_produit,prix,quantite,description)
                                values(?,?,?,?,?)
        ''',(self.id,self.nom,self.prix,self.quantite,self.description)) #!chkit n7ydo self
        self.connexion.commit()
        self.connexion.close()

    
    def modifier_produit(self,nv_nom,nv_prix,nv_quantite,nv_description,id):
        self.connexion = sqlite3.connect('magasin.db')
        self.cursor = self.connexion.cursor()
        self.cursor.execute(
            "UPDATE produit SET nom = ?, prix = ?, quantite = ?, desciprtion = ? WHERE id = ?",
                            (nv_nom,nv_prix,nv_quantite,nv_description,id))
        self.connexion.commit()
        self.connexion.close()

    def chercher_produit(self,id):
        self.connexion = sqlite3.connect('magasin.db')
        self.cursor = self.connexion.cursor()
        self.cursor.execute('''
                SELECT COUNT(*) FROM produit WHERE id = ?
                            ''',id)
        self.result = self.cursor.fetchall()
        self.connexion.close()
        return self.result[0] > 0 #!je pense que n'est pas necessaire de [0]

    def suprimmer_produit(self,id):
        self.connexion = sqlite3.connect('magasin.db')
        self.cursor = self.connexion.cursor()
        self.cursor.execute('DELETE FROM produit WHERE id =?',(id,))
        self.connexion.commit()
        self.connexion.close()

t1_p = Produit_sql()
t1_p.creer_db_produit()