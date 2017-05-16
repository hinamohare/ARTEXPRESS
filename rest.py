import pymongo
import base64

import pymongo
from flask import Flask, send_file, request, json, jsonify, render_template
import api
from bson.json_util import dumps

def insert():
    with open("C:\Users\Hina\Desktop\home\IMG_4443.JPG", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    print encoded_string
    dbconnection = pymongo.MongoClient()
    dbname = dbconnection.cmpe280
    collection = dbname.test

    abc = collection.insert({"image": encoded_string})

def retrieve():
    dbconnection = pymongo.MongoClient()
    dbname = dbconnection.cmpe280
    collection = dbname.test
    data = collection.find()
    data1 = json.loads(dumps(data))
    img = data1[0]
    img1 = img['image']
    decode = img1.decode()
    print decode
    img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(decode)
    print img_tag

#insert()
retrieve()