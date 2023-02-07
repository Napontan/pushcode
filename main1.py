from pymongo import MongoClient,collection
from dotenv import load_dotenv
from os import getenv


load_dotenv(".env")
paswd = getenv("passwd")
client = MongoClient(f"mongodb://exceed15:{paswd}@mongo.exceed19.online:8443")

data = [{
    "stdId": "631054000",
    "stdName": "person",
    "course_name": 'subject',
    "grade": 1,
    "unit": 1
},{
    "stdId": "631054001",
    "stdName": "person",
    "course_name": 'subject1',
    "grade": 1.5,
    "unit": 1
},{
    "stdId": "631054002",
    "stdName": "person2",
    "course_name": 'subject2',
    "grade": 2.5,
    "unit": 3
},{
    "stdId": "631054003",
    "stdName": "person3",
    "course_name": 'subject2',
    "grade": 2.5,
    "unit": 3
},
{
    "stdId": "631054004",
    "stdName": "person4",
    "course_name": 'subject3',
    "grade": 4,
    "unit": 3
}]


db = client["exceed15"]
colletion: collection.Collection = db["sample_airbnb"]
new_value = colletion.update_many({"course_name": "subject2"},{"$set":{"unit":1}})

ori_data = colletion.find().limit(5)
for i in ori_data:
    print(i)