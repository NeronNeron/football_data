#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program do:
# 1.takes data from default.yaml 
# 2.makes a request to api.football-data.org
# 3.saves leages to default.yaml

import yaml
from attrdict import AttrDict
import requests 
import json

def create_default():
#Load data from default.yaml
	f = open('default.yaml', 'r')
# use safe_load instead load
	default_ = yaml.safe_load(f)
	default = AttrDict(default_)
	f.close()


	#print("Keys of default: ", default.keys())
	#print(default)
	#print(default.API_key)

	url = default.base_url


	headers={'X-Auth-Token': default.API_key, 'X-Response-Control': 'full'}
	r = requests.get(url, headers=headers)
	#print(r)
	#print(r.content)

	if r.status_code == 200:
		r.listj = json.loads(r.content)
		r.list = yaml.safe_load(r.content)  # solve problem with unicode
		r.readable = json.dumps(r.listj, indent=4)
		#print(r.readable) 
		print type(r.list)

#Take league's names and links to make dict
		leagues_list = [item['caption'] for item in r.list]
		links = [item['_links'] for item in r.list]
		leagues = dict(zip(leagues_list, links))
		default_['leagues'] = leagues
		#print(default_)

# to write readable result to new file
		#w = open("comparison2.txt", "w")
		#w.writelines(r.readable)
		#w.close()
# create config.yaml
		new = open('config.yaml', "w")
		yaml.dump(default_, new)
		new.close()


	else:
		raise AttributeError('Problem with connection or bad URL given')
	
create_default()



