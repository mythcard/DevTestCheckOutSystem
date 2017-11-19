import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.checkOut
#productCatalog = db.productCatalog


