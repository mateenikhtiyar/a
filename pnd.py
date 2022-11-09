import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://mateen:asdf@cluster0.yqoowcc.mongodb.net/?retryWrites=true&w=majority")
db = cluster['base']
collection = db['colection']
post = {
    'id':1,
    'name':'talha',
    'age':18
}

post2 = {
    'id':2,
    'name':'tayab',
    'age':22
}

collection.insert_many([post,post2])

m=collection.find({'id':2})
for c in m:
   print(c)

m=collection.find({'id':2})
for c in m:
    print(c['name'])


i={
    'id':2  
}
m=collection.find(i)
for c in m:
    print(c['name'])

m=collection.find_one({'id':1})
print(m)

collection.update_one( { 'id': 1 }, { set: { 'name': 'usman' } } )

collection.update_many({}, { inc: { 'name': 1 } })

collection.delete_one({ 'id': 1 })

collection.delete_many({ 'id' })
collection.drop()







