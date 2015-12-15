#!/usr/bin/env python
# -*- coding: latin-1-*-
import sqlite3
from peewee import *
import yaml
from attrdict import AttrDict


def create_database():
#Load data from config.yaml
	f = open('config.yaml', 'r')
# use safe_load instead load
	config_ = yaml.safe_load(f)
	config = AttrDict(config_)
	f.close()
	
#creates database, name is tacking from config.yaml
	#conn = sqlite3.connect('{}'.format(config.database_name))

#here we'll prepare leagues list, later we'll use items for tablem names
	leagues = []
	for key in config_['leagues']:
		if key != 'Champions League 2015/16':
			
			leagues.append(key)
	print leagues
	
	#conn = sqlite3.connect('{}'.format(config.database_name))
	#c = conn.cursor()
	#for item in leagues:
	#	print type(item)
	#	c.execute("CREATE TABLE {}(rank, team, teamId, points, goals, goalsAgainst, goalDifference)".format(item))



	db = SqliteDatabase('{}'.format(config.database_name))

	class Table(Model):
		rank = CharField()
		team = CharField()
		teamId = CharField()
		points = CharField()
		goals = CharField()
		goalsAgainst = CharField()
		goalDifference = CharField()

		class Meta:
			database = db

	conn = sqlite3.connect('soccer.db')


#db.connect()
#db.create_tables(Table)

create_database()