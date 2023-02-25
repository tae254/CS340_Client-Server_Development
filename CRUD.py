from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.

        self.client = MongoClient('mongodb://%s:%s@localhost:55794' % (username, password), authSource = "AAC")
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
                self.database.animals.insert(data)
                data = data
                #print(data)
        else:
                raise Exception("Data parameter is empty")
                data = false
        return data

# Create method to implement the R in CRUD.
    def read(self, data):
        cursor = self.database.animals.find(data, {"_id": False})
        #print(cursor)
        return cursor
    
    def readAll(self, data = None):
        if data:
            cursor = self.database.animals.find(data, {"_id": False})
            #print(cursor)
        else:
            cursor = self.database.animals.find({}, {"_id": False})
            #print(cursor)
             
        return cursor
    
# Create method to implement the U in CRUD
    def update(self, data, dataUpdate):
        if data:
            cursor = self.database.animals.update_one(data, dataUpdate)
            #print(cursor)
            return cursor
        
        else:
            raise Exception("Nothing to change!")
                
# Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            if data:
                result = self.database.animals.delete_one(data)
                #print(result)
        else:
            raise Exception("No data to delete")
        