from app import mongoConnect
import Transaction


def getAllProduct():
    productcatalog = mongoConnect.db.productCatalog
    productcur = productcatalog.find()

    return productcur


def getItems(productCode):
    productcatalog = mongoConnect.db.productCatalog
    productName = productcatalog.find({'productCode': productCode}, {'productName': '2'})
    productPrice = productcatalog.find({'productCode': productCode}, {'productPrice': '3'})
    return productCode, productName, productPrice


def buildTransactionId():
    transactionDetails = mongoConnect.db.transactionDetails
    id = transactionDetails.insert({})
    return id


"""
def addItemToTransaction(trans):
    ## strip the list of items and store it as an array of product code, name and price

def getTransaction():
    trans = Transaction.Item()
    ## get list of items and add it to the transaction
    return trans

"""

