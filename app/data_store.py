import json
from pymongo import MongoClient


class post_data:
    def __init__(self) -> None:
        pass

    def pydata(self, json_file):

        myclient = MongoClient('localhost:27017')

        db = myclient["mydatabase"] # use data base named "mydatabase"

        Collection = db["data"] # create collection named "data"

        
        with open(json_file, 'r',  encoding='utf-8') as file:
            file_data = json.load(file)
            print(file_data)
        
        if isinstance(file_data, list):
            Collection.insert_many(file_data)

        else:
            Collection.insert_one(file_data)

        return db
        
    def getdata(self):

        myclient = MongoClient('localhost')

        db = myclient["mydatabase"] 

        Collection = db["data"]

        documents = Collection.find()

        return list(documents)

    def getdetails(self, URL):

        myclient = MongoClient('localhost')

        db = myclient["mydatabase"]
        Collection = db["data"]
        x = Collection.find({'url_page': URL})
        
        return list(x)
