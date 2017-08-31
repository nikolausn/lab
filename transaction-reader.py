import csv;
#import json;
#import os;

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
        
        # Long way, copy selective attributes only
#        customer[row["custId"]] = {};
#        custRow = customer[row["custId"]];
#        custRow["custId"] = row["custId"];
#        custRow["custName"] = row["custName"];
#        custRow["address"] = row["address"];
#        custRow["city"] = row["city"];
#        custRow["states"] = row["states"];
#        custRow["zipcode"] = row["zipcode"];
    i = i + 1;
customer["length"] = i;

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
stores["length"] = i;

# read transaction file
reader = csv.DictReader(transactionFile, transactionField,delimiter=',');
i = 0;
groupCustIdManager = {};

print('Join Operation between customer, store, and transaction:')
for row in reader:
    if (i!=0):
        myCust = customer[row['custId']];
        myStore = stores[row['storeNumber']];
        print("customer name: %s, transaction date: %s, transaction amount: %s, store manager: %s" %(myCust['custName'],row['transDate'],row['amount'],myStore['storeManager']));
        
        #group by customer id and manager
        #check if not exist customerId
        if(not row['custId'] in groupCustIdManager.keys()):
            #init customer
            groupCustIdManager[row['custId']] = {};
            groupCustIdManager[row['custId']][myStore['storeManager']] = {};
            groupCustIdManager[row['custId']][myStore['storeManager']]['amount'] = row['amount'];
            groupCustIdManager[row['custId']][myStore['storeManager']]['count'] = 1;
            groupCustIdManager[row['custId']][myStore['storeManager']]['custname'] = myCust['custName'];
        else:
            #check if not exist manager
            if(not myStore['storeManager'] in groupCustIdManager[row['custId']].keys()):
                #init manager
                groupCustIdManager[row['custId']][myStore['storeManager']] = {};
                groupCustIdManager[row['custId']][myStore['storeManager']]['amount'] = row['amount'];
                groupCustIdManager[row['custId']][myStore['storeManager']]['count'] = 1;
                groupCustIdManager[row['custId']][myStore['storeManager']]['custname'] = myCust['custName'];                
            else:
                #add amount to existing grouping value
                groupCustIdManager[row['custId']][myStore['storeManager']]['amount'] = groupCustIdManager[row['custId']][myStore['storeManager']]['amount'] + row['amount'];
                groupCustIdManager[row['custId']][myStore['storeManager']]['count'] = groupCustIdManager[row['custId']][myStore['storeManager']]['count'] + 1;
    i = i + 1;

#print groupCustIdManager
print("\nGroup by customer id and manager: ")
for attrCust,valueCust in groupCustIdManager.items():
    for attrStore,valueStore in valueCust.items():
        print("customer id: %s, custname: %s, manager: %s, sum amount: %s, trans count: %s" %(attrCust,valueStore['custname'],attrStore,valueStore['amount'],valueStore['count']));
