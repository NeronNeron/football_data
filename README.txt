This program will get a lot of data from http://api.football-data.org
and storeit in local database.
Not now, in near future.

You will need installed: Python2.7, pyyaml, sqlite3, peewee.
----------------------------------------------------------------------
Before starting prepare default.yaml with structure:

base_url: 'http://api.football-data.org/v1/soccerseasons'
API_key: Your API KEY
database_name: name of DB you want to create
----------------------------------------------------------------------
Steps:
1. Module create_config.py takes data from default.yaml and makes a request. In a result we get list of available campionships and links 
(league table, teams, fixtures) per each league. This data is stored in newly created config.yaml.

2. Module make_req.py takes links from config.yaml and make requests to get all needed data. Result will be converted to csv.

3. Module createDB.py will create database and fill it

Later run.py will be added.


