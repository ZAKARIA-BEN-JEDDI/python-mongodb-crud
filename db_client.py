import sqlite3

def creer_db_client():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS client(
                            id_client INTEGER NOT NULL PRIMARY KEY,
                            nom TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            mdp TEXT NOT NULL,
                            address_laivraison TEXT NOT NULL
                        );
        ''')
    connexion.commit()
    connexion.close()
    
def get_all_client():
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM client')
    all_client = cursor.fetchall()
    connexion.close()
    return all_client

def ajouter(id, nom, email, mdp, adress):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
                        INSERT INTO client (id_client,nom, email, mdp,address_laivraison) values(? ,? ,? ,? ,?)
                        ''',(id, nom, email, mdp, adress))
    connexion.commit()
    connexion.close()

def modifier(nv_nom ,nv_email ,nv_mdp ,nv_adress, id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
                        UPDATE client
                        SET nom == ?, email = ?, mdp = ?, address_laivraison = ?
                        WHERE id_client = ?
                ''',(nv_nom ,nv_email ,nv_mdp ,nv_adress, id))
    connexion.commit()
    connexion.close()

def chercher_client(id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
        SELECT COUNT(*) FROM client WHERE id_client = ?
    ''', (id,))
    result = cursor.fetchone()
    connexion.close()
    return int(result[0]) > 0

def chercher_client_email(email):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
        SELECT * FROM client WHERE email = ?
    ''', (email,))
    all_client = cursor.fetchall()
    connexion.close()
    return all_client

def chercher_client_nom(nom):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('''
        SELECT * FROM client WHERE nom = ?
    ''', (nom,))
    result = cursor.fetchall()
    connexion.close()
    return result

def suprimmer_client(id):
    connexion = sqlite3.connect('magasin.db')
    cursor = connexion.cursor()
    cursor.execute('DELETE FROM client WHERE id_client =?',(id,))
    connexion.commit()
    connexion.close()

creer_db_client()