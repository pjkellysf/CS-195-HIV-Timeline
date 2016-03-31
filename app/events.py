import datetime
from peewee import *

db = SqliteDatabase('events.db')

class Event(Model):
	year = DateTimeField(default=0)
	deaths = IntegerField(default=0)
	health = TextField()
	international = TextField()
	political = TextField()
	social = TextField()
	celeb = TextField()

	class Meta:
		database = db

def initialize():
	db.connect()
	db.create_tables([Event], safe=True)
	return db;

def insertRow(dataList):
	Event.create(
		year = dataList[0],
		deaths = int(dataList[1].replace(',', '')),
		health = dataList[2],
		international = dataList[3],
		political = dataList[4],
		social = dataList[5],
		celeb = dataList[6]
		)

def displayTable():
	for event in Event.select():
		print(event)

if __name__ == '__main__':
	initialize()
	displayTable()

	