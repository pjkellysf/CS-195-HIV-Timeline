from peewee import *

db = SqliteDatabase('events.db')

class Event(Model):
	year = IntegerField(default=0)
	deaths = IntegerField(default=0)
	health = CharField()
	international = CharField()
	political = CharField()
	social = CharField()
	celeb = CharField()

	class Meta:
		database = db


if __name__ == '__main__':
	db.connect()
	db.create_tables([Event], safe=True)