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

def createDb():
	db.connect()
	db.create_tables([Event], safe=True)
	return db;
