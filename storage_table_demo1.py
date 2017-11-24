# File Modified by Shailesh Beri Nov 24 13:13 PM
import string,random,time,azurerm,json
from azure.storage.table import TableService, Entity

# Define variables to handle Azure authentication
auth_token = azurerm.get_access_token_from_cli()
subscription_id = azurerm.get_subscription_from_cli()

# Define variables with random resource group and storage account names
resourcegroup_name = 'sb06'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
storageaccount_name = 'sb06'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
location = 'eastus'

###
# Create the a resource group for our demo
# We need a resource group and a storage account. A random name is generated, as each storage account name must be globally unique.
###
response = azurerm.create_resource_group(auth_token, subscription_id, resourcegroup_name, location)
if response.status_code == 200 or response.status_code == 201:
    print('Resource group: ' + resourcegroup_name + ' created successfully.')
else:
    print('Error creating resource group')

# Create a storage account for our demo
response = azurerm.create_storage_account(auth_token, subscription_id, resourcegroup_name, storageaccount_name,  location, storage_type='Standard_LRS')
if response.status_code == 202:
    print('Storage account: ' + storageaccount_name + ' created successfully.')
    time.sleep(2)
else:
    print('Error creating storage account')


###
# Use the Azure Storage Storage SDK for Python to create a Table
###
print('\nLet\'s create an Azure Storage Table to store some data.')
raw_input('Press Enter to continue...')

# Each storage account has a primary and secondary access key.
# These keys are used by applications to access data in your storage account, such as Tables.
# Obtain the primary storage access key for use with the rest of the demo

response = azurerm.get_storage_account_keys(auth_token, subscription_id, resourcegroup_name, storageaccount_name)
storageaccount_keys = json.loads(response.text)
storageaccount_primarykey = storageaccount_keys['keys'][0]['value']

# Create the Table with the Azure Storage SDK and the access key obtained in the previous step
table_service = TableService(account_name=storageaccount_name, account_key=storageaccount_primarykey)
response = table_service.create_table('itemstable')
if response == True:
    print('Storage Table: itemstable created successfully.\n')
else:
    print('Error creating Storage Table.\n')

time.sleep(1)


###
# Use the Azure Storage Storage SDK for Python to create some entries in the Table
###
print('Now let\'s add some entries to our Table.\nRemember, Azure Storage Tables is a NoSQL datastore, so this is similar to adding records to a database.')
raw_input('Press Enter to continue...')

# Each entry in a Table is called an 'Entity'. 

# Here, we add an entry for first pizza with two pieces of data - the name, and the cost
#
# A partition key tracks how like-minded entries in the Table are created and queried.
# A row key is a unique ID for each entity in the partition
# These two properties are used as a primary key to index the Table. This makes queries much quicker.

# Shailesh Beri - Pizza Related lines are commented out

# pizza = Entity()
# pizza.PartitionKey = 'pizzamenu'
# pizza.RowKey = '001'
# pizza.description = 'Pepperoni'
# pizza.cost = 18
# table_service.insert_entity('itemstable', pizza)
# print('Created entry for pepperoni...')

# pizza = Entity()
# pizza.PartitionKey = 'pizzamenu'
# pizza.RowKey = '002'
# pizza.description = 'Veggie'
# pizza.cost = 15
# table_service.insert_entity('itemstable', pizza)
# print('Created entry for veggie...')

# pizza = Entity()
# pizza.PartitionKey = 'pizzamenu'
# pizza.RowKey = '003'
# pizza.description = 'Hawaiian'
# pizza.cost = 12
# table_service.insert_entity('itemstable', pizza)
# print('Created entry for Hawaiian...\n')


# Shailesh Beri - Add code here to populate partition with cars using dealership scenario and with characteristics [make, model, year, color and price] instead of Pizza


cars = Entity()
cars.PartitionKey = 'carstype'
cars.RowKey = '001'
cars.make = 'BMW'
cars.model = 'X3'
cars.year =  2017
cars.color = 'Red'
cars.price = 51000
table_service.insert_entity('itemstable', cars)
print('Created entry for BMW X3...')

cars = Entity()
cars.PartitionKey = 'carstype'
cars.RowKey = '002'
cars.make = 'Audi'
cars.model = 'Q5'
cars.year =  2017
cars.color = 'White'
cars.price = 47000
table_service.insert_entity('itemstable', cars)
print('Created entry for Audi Q5...')

cars = Entity()
cars.PartitionKey = 'carstype'
cars.RowKey = '003'
cars.make = 'Mercedes'
cars.model = 'GLC300'
cars.year =  2017
cars.color = 'Black'
cars.price = 50700
table_service.insert_entity('itemstable', cars)
print('Created entry for Mercedes GLC300...')

cars = Entity()
cars.PartitionKey = 'carstype'
cars.RowKey = '004'
cars.make = 'Porsche'
cars.model = 'Macan'
cars.year =  2017
cars.color = 'Blue'
cars.price = 57000
table_service.insert_entity('itemstable', cars)
print('Created entry for Porsche Macan...')

# End code for Cars

# Shailesh Beri - Add code here to populate yet another partition with coffee shop inventory. Coffee is characterized by the brand, flavor, size of the cup and price per cup

coffee = Entity()
coffee.PartitionKey = 'coffeemenu'
coffee.RowKey = '001'
coffee.brand = 'Starbucks'
coffee.flavor = 'Dark Roast'
coffee.cupsize =  '12 Oz'
coffee.price = 5.75
table_service.insert_entity('itemstable', coffee)
print('Created entry for Starbucks Dark Roast 12 Oz...')

coffee = Entity()
coffee.PartitionKey = 'coffeemenu'
coffee.RowKey = '002'
coffee.brand = 'Seattles Best'
coffee.flavor = 'Medium Roast'
coffee.cupsize =  '12 Oz'
coffee.price = 5.25
table_service.insert_entity('itemstable', coffee)
print('Created entry for Seattles Best Medium Roast 12 Oz...')

coffee = Entity()
coffee.PartitionKey = 'coffeemenu'
coffee.RowKey = '003'
coffee.brand = 'Petes'
coffee.flavor = 'Dark Roast'
coffee.cupsize =  '12 Oz'
coffee.price = 5.65
table_service.insert_entity('itemstable', coffee)
print('Created entry for Petes Dark Roast 12 Oz...')

# End code for Coffee Shop Inventory

# A partition key tracks how like-minded entries in the Table are created and queried.
# A row key is a unique ID for each entity in the partition
# These two properties are used as a primary key to index the Table. This makes queries much quicker.

clothing = Entity()
clothing.PartitionKey = 'clothingstore'
clothing.RowKey = '005'
clothing.sku = 'BLK203123'
clothing.item = 'sweater'
clothing.cost = 22.99
table_service.insert_entity('itemstable', clothing)
print('Created entry for a Sweater...\n')
time.sleep(1)

clothing = Entity()
clothing.PartitionKey = 'clothingstore'
clothing.RowKey = '006'
clothing.sku = 'BLK203143'
clothing.item = 'jeans'
clothing.cost = 55.99
table_service.insert_entity('itemstable', clothing)
print('Created entry for Jeans...\n')
time.sleep(1)

###
# Use the Azure Storage Storage SDK for Python to query for entities in our Table
###
print('With some data in our Azure Storage Table, we can query the data.\nLet\'s see what the carstype looks like.')
raw_input('Press Enter to continue...')

# In this query, you define the partition key to search within, and then which properties to retrieve
# Structuring queries like this improves performance as your application scales up and keeps the queries efficient
items = table_service.query_entities('itemstable', filter="PartitionKey eq 'carstype'", select='make,model,year,color,price')
for item in items:
    print('make: ' + item.make)
    print('model: ' + item.model)
    print('year: ' + str(item.year))
    print('color: ' + item.color)
    print('price: ' + str(item.price) + '\n')

# items = table_service.query_entities('itemstable', filter="PartitionKey eq 'clothingstore'", select='description,price')
# for item in items:
#     print('Name: ' + item.description)
#     print('Price: ' + str(item.price) + '\n')

# time.sleep(1)


###
# This was a quick demo to see Tables in action.
# Although the actual cost is minimal (fractions of a cent per month) for the three entities we created, it's good to clean up resources when you're done
###
print('\nThis is a basic example of how Azure Storage Tables behave like a database.\nTo keep things tidy, let\'s clean up the Azure Storage resources we created.')
raw_input('Press Enter to continue...')

response = table_service.delete_table('itemstable')
if response == True:
    print('Storage table: itemstable deleted successfully.')
else:
    print('Error deleting Storage Table')

response = azurerm.delete_resource_group(auth_token, subscription_id, resourcegroup_name)
if response.status_code == 202:
    print('Resource group: ' + resourcegroup_name + ' deleted successfully.')
else:
    print('Error deleting resource group.')
