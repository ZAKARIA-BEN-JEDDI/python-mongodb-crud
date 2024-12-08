# import pymongo

# # Connexion à MongoDB
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# # Connexion à la base de données existante PythonMongodb
# mydb = myclient["PythonMongodb"]

# # Connexion à la collection client
# client_collection = mydb["client"]

# # Insérer un document (exemple)
# new_client = {
#     "_id": 2,
#     "prenom": "Fatima",
#     "tel": "0611223344",
#     "adress_laivraison": "Casablanca Maarif"
# }
# insert_result = client_collection.insert_one(new_client)
# print(f"Document inséré avec l'ID : {insert_result.inserted_id}")

# # Afficher tous les documents de la collection client
# print("Documents dans la collection client :")
# for client in client_collection.find():
#     print(client)


import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

PythonMongodb = myclient["PythonMongodb"]

client_collection = PythonMongodb['client']

# TODO initialisation des key de document
# id = int(input("enterer un id : "))
# prenom = (input("entrer le prenom de client : ")) 
# tel = (input("entrer le tel de client : ")) 
# adress_laivraison = (input("entrer le adress_laivraison de client : "))

# print("id de client : ", id)
# print("prenom de client : ", prenom)
# print("tel de client : ", tel)
# print("adress laivresson de client : ", adress_laivraison)

# client_collection.insert_one({'_id':id,'prenom':prenom,'tel':tel,'adress_laivraison':adress_laivraison})

allClient = client_collection.find()

for client in allClient:
  id = client.get('_id', "Inconnu")
  prenom = client.get('prenom', "Inconnu")
  tel = client.get('tel', "Inconnu")
  adress_laivraison = client.get('adress_laivraison', "Inconnu")

  print(id)
  print(prenom)
  print(tel)
  print(adress_laivraison)
  print("-"*30)

