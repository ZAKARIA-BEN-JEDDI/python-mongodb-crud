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

allClient = client_collection.find()
for client in allClient:
  print(client)











