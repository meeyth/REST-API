from pymongo import MongoClient
import datetime
from model.user import userSchema

# connecting to mongo db
client = MongoClient('mongodb://localhost:27017/')

# creating database
db = client['user-db']

# creating collection
if "user-collection" not in db.list_collection_names():
    collection = db.create_collection("user-collection", validator=userSchema)
else:
    collection = db["user-collection"]


def get_data(_id):
    return collection.find_one({'_id': _id})


def post_data(body):
    time = datetime.datetime.now()
    body |= {"createdAt": time.strftime("%Y-%m-%d %H:%M:%S")}
    collection.insert_one(body)


def put_data(body, _id):
    time = datetime.datetime.now()
    if (prev := collection.find_one({'_id': _id})):
        body |= {"createdAt":  prev["createdAt"]}
        body |= {"_id": _id, "updatedAt": time.strftime("%Y-%m-%d %H:%M:%S")}
        collection.replace_one(prev, body)
    else:
        body |= {"_id": _id, "createdAt": time.strftime("%Y-%m-%d %H:%M:%S")}
        collection.insert_one(body)


def patch_data(body, _id):
    time = datetime.datetime.now()
    if (prev := collection.find_one({'_id': _id})):
        body |= {"updatedAt": time.strftime("%Y-%m-%d %H:%M:%S")}
        to_update = {'$set': body}
        collection.update_one(prev, to_update)
        updated = collection.find_one({'_id': _id})
        return updated
    return None


def delete_data(_id):
    record = {'_id': _id}
    if (document := collection.find_one(record)):
        collection.delete_one(record)
        return document
    return None


def collection_len():
    return collection.count_documents({})
