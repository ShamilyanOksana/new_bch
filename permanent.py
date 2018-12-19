
create_table_roles = '''
CREATE TABLE IF NOT EXISTS roles(
id_role INTEGER PRIMARY KEY AUTOINCREMENT,
role VARCHAR
)'''

create_table_IK = '''
CREATE TABLE IF NOT EXISTS IK(
id_IK INTEGER PRIMARY KEY AUTOINCREMENT, 
IK VARCHAR
)'''

create_table_open_account = '''
CREATE TABLE IF NOT EXISTS open_account(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
fio VARCHAR,
role INTEGER,
IK INTEGER,
auditor INTEGER,
admin INTEGER,
telephone VARCHAR,
address VARCHAR,
OKo VARCHAR,
SOKo VARCHAR,
SZKo VARCHAR
)'''

create_table_open_voting = '''
CREATE TABLE IF NOT EXISTS open_voting (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
question INTEGER,
role INTEGER,
candidate_OKo VARCHAR,
start DATETIME,
finish DATETIME,
result VARCHAR
)'''

create_table_open_voting_decision = '''
CREATE TABLE IF NOT EXISTS open_voting_decision(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
ID_gol INTEGER,
OKo VARCHAR,
answer integer
)'''

create_table_close_account = '''
CREATE TABLE IF NOT EXISTS close_account(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
role INTEGER,
OKz VARCHAR,
SOKz VARCHAR,
SZKz VARCHAR
)'''

create_table_close_voting = '''
CREATE TABLE IF NOT EXISTS close_voting(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
question VARCHAR,
role INTEGER,
start DATETIME,
finish DATETIME,
result VARCHAR
)'''

create_table_close_voting_decision = '''
CREATE TABLE IF NOT EXISTS close_voting_decision(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
ID_gol INTEGER,
OKz VARCHAR,
answer INTEGER
)'''
