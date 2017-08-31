# lab-python-multifilereader
Simple example to combine dataset, I used hash method in python to minimize the complexity.

The case of this program is to join 3 CSV files which are:
- customers.dat: stores customer data (custId/pk, custName, address, city, states, zipcode)
- stores.dat: contains information about the store that customers have transaction with (storeID/pk, storeManager, address, city, state, zipcode)
- transactions.dat: each row represents transaction information that a customer has done in a store (transactionID, transDate, custId/fk-customers, storeNumber/fk-stores, amount)

There are two goals of this join operation:
1. Print the transaction information that include the customer name and store manager name
2. Aggregate / sum the transaction amount and total transactions happened for a customer and manager respectively.

Just need a CSV library that usually is built in the python 3. Just fair warning, I didn't have any error handling in the process.
