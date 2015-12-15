#!/usr/bin/env python
# -*- coding: latin-1 -*-
# This program do:
# 1.takes urls from config
# 2.makes requests
# 3.write results to database

import yaml
from attrdict import AttrDict
import requests 
import json

def do_job():
	#Load data from config.yaml
	f = open('config.yaml', 'r')
# use safe_load instead load
	config_ = yaml.safe_load(f)
	config = AttrDict(config_)
	f.close()

	#print(type(config_['leagues']))
	#print(config_['leagues']['Champions League 2015/16']['leagueTable']['href'])

#here we'll prepare league: table-links  dictionary
	leags = []
	links = []

	for key in config_['leagues']:
		leags.append(key)
	for name in leags:
		links.append(config_['leagues'][name]['leagueTable']['href'])
#Here we have dict with leagues name and proper link
	leagues_tables = dict(zip(leags, links))

	#print(leagues_tables)


#Here we start to make reguests to get actual table per each league
	headers={'X-Auth-Token': config.API_key, 'X-Response-Control': 'minified'} #it will be used for all requests

	

	for key in leagues_tables:
		if key != 'Champions League 2015/16':  #becouse Champions League don't have agregated table, also link is broken
			r = requests.get(leagues_tables[key], headers=headers)
			r.list = json.loads(r.content)
			print type(r.list)
			for item in r.list['standing']:
				
				print(item['team'])
				
				

	#print(r.list['standing'])



#makes readable repr. and write to comparison3.txt. Don't relate to main purpose of this module
'''
	r.listj = json.loads(r.content)
	r.readable = json.dumps(r.listj, indent=4)

	w = open("comparison3.txt", "w")
	w.writelines(r.readable)
	w.close()
'''

do_job()