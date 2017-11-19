from app import app
from app import mongoConnect
import Transaction
import DBConnect
from flask import render_template, request, url_for, redirect, session
import pickle



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/addItem", methods=["GET", "POST"])
def addItem():
    allItemsAdded = []
    all_products = []
    index_error = None
    if request.method == 'GET':
        session.clear()
        productcur = DBConnect.getAllProduct()
        data = list(productcur)
        all_products = list()
        for row in data:
            all_products.append(row)


        return render_template('index.html', all_products=all_products)
    elif request.method == 'POST':
        allItemsAdded = []
        allItemsAdded = session.get('sub_list', None)
        button_value = str(request.form['submit'])
        itemName = str(request.form['item'])


        if(button_value == 'add'):
            if allItemsAdded is None:
                allItemsAdded = []
            allItemsAdded.append(itemName)

        elif(button_value == 'delete'):
            ## check DB catalog and delete
            allItemsAdded.remove(itemName)
            ## delete here
            #itm = Item.getItem(itemName)
            #print(itm.productName)
            #trans.deleteItem(itm)

        productcur = DBConnect.getAllProduct()
        data = list(productcur)
        all_products = list()
        for row in data:
            all_products.append(row)


        session['sub_list'] = allItemsAdded
        return render_template('index.html', all_products=all_products, lstOfItems = allItemsAdded)

@app.route('/all_items_trans', methods =['GET'])
def all_items_trans():
    allItemsAdded = []
    allItemsAdded = session.get('sub_list', None)
    trans = Transaction.Transaction()
    trans.addItem(allItemsAdded)
    trans.addBOGOItems()
    trans.addCHMKItems()
    lstOfItemsproductCode, lstOfItemsproductName, lstOfItemsproductPrice = trans.getListOfItems()
    return render_template('landingPage.html', lstOfItemsproductCode = lstOfItemsproductCode, lstOfItemsproductName= lstOfItemsproductName, lstOfItemsproductPrice = lstOfItemsproductPrice)


