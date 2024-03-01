from pymongo import MongoClient
from flask import Flask
from flask import render_template

cluster = MongoClient("mongodb+srv://bezawadaphilip:Md101627@cluster0.0rdhh3c.mongodb.net/")
database = cluster['Db1']
collection = database['cl1']

app = Flask(__name__)

# operations , api's--
@app.route("/")
def hello_world():
    return render_template("login.html")

@app.route("/insertOne")   # the endpoint name is (user_defined)
def insertone():
    collection.insert_one({"name":"MongoDb"})
    return "Data is inserted"
# display data

@app.route("/display")
def displayData():
    data = collection.find()     #data stores in object form , so required to change into json or str, in list
    l = []
    for record in data: 
        x = {}
        x['name']=record['name']
        l.append(x)
    return l

data= collection.find()
for record in data:
    for key, value in record.items():
        print(f"{key}: {value}")

@app.route("/deleteMany")
def deletemany():
    query = {"$or":[{"name":"MongoDB"}]}
    result = collection.delete_many(query)
    return f"{result.deleted_count} records deleted"

@app.route("/deleteOne")
def deleteOne():
    query = {"name":"MongoDb"}
    result = collection.delete_one(query)
    return f"{result.deleted_count} records deleted"

@app.route("/insertMany")
def insertMany():
    query = [{"name":"philip"},{"name":"bejawada"}]
    result = collection.insert_many(query)
    return f"{query} these records are inserted"

@app.route("/updateOne")
def updateone():
    before = {"name":"bejawada"}
    after = {"$set":{"name":"vijayawada"}}
    collection.update_one(before,after)
    return f"{before} is updated to {after}"


@app.route("/updateMany")
def updatemany():
    before = {"name": {"$in": ["philip", "vijayawada"]}}
    after = {"$set": {"name": "bejawada"}}
    collection.update_many(before,after)
    return f"{before} is updated to {after}"

if __name__ == "__main__":
    app.run(debug=True)