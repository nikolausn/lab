#!/usr/bin/python
import csv;
import json;
import os;

customerFile = open('customers.dat', 'r');
storesFile = open('stores.dat', 'r');
transactionFile = open('transactions.dat','r');

customerField = ("custId", "custName", "address", "city", "states", "zipcode");
storesField = ("storeID", "storeManager", "address", "city", "state", "zipcode");
transactionField = ("transactionID", "transDate", "custId", "storeNumber", "amount");

# read customer references and put it on memory
reader = csv.DictReader(customerFile, customerField,delimiter=',');
customer = {};
i = 0
for row in reader:
    if (i!=0):        
        # Short way, copy the object
        customer[row["custId"]] = row.copy();
        
        # Long way, copy selective attribtue only
#        customer[row["custId"]] = {};
#        custRow = customer[row["custId"]];
#        custRow["custId"] = row["custId"];
#        custRow["custName"] = row["custName"];
#        custRow["address"] = row["address"];
#        custRow["city"] = row["city"];
#        custRow["states"] = row["states"];
#        custRow["zipcode"] = row["zipcode"];
    i = i + 1;
customer["length"] = i-1;

# read stores references and put it on memory
reader = csv.DictReader(storesFile, storesField,delimiter=',');
stores = {};
i = 0
for row in reader:
    if (i!=0):        
        # Short way, copy the object
        stores[row["storeID"]]  = row.copy();
        
        # Long way, copy selective attribtue only        
#        stores[row["storeID"]] = {};
#        storeRow = stores[row["storeID"]];
#        storeRow["storeID"] = row["storeID"];
#        storeRow["storeManager"] = row["storeManager"];
#        storeRow["address"] = row["address"];
#        storeRow["city"] = row["city"];
#        storeRow["state"] = row["state"];
#        storeRow["zipcode"] = row["zipcode"];
    i = i + 1;
stores["length"] = i-1;

# read transaction file
reader = csv.DictReader(transactionFile, transactionField,delimiter=',');
i = 0;
for row in reader:
    if (i!=0):
        myCust = customer[row['custId']];
        myStore = stores[row['storeNumber']];
        print "customer name: %s, transaction date: %s, transaction amount: %s, store manager: %s" %(myCust['custName'],row['transDate'],row['amount'],myStore['storeManager']);
    i = i + 1;


        
    




