# Day 24 Task
# Gokul Dhaskana Murthy

import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="free",
  buffered = True,
)

dbse = mydb.cursor()
dbse.execute('Drop table json_data')
dbse.execute('Create table json_data(job_text text, id_int int, Bool boolean, salary_float float, name_string text)')

test_json = json.loads(json.dumps(
[{
    "job_text": "Designer",
    "id_int": 12,
    "Bool": True,
    "salary_float": 654.2156,
    "name_string": "Gokul"
    },
    {
    "job_text": "Teacher",
    "id_int": 10,
    "Bool": False,
    "salary_float": 8718.28,
    "name_string": "Dhakshana Murthy"
    },]
    )
)

values = [list(x.values()) for x in test_json]
# print(values)


columns = [list(x.keys()) for x in test_json][0]

values_str = ""

for i, record in enumerate(values):

    val_list = []
   
    for v, val in enumerate(record):
        if type(val) == str:
            val = "'{}'".format(val.replace("'", "''"))
        val_list += [ str(val) ]

    values_str += "(" + ', '.join( val_list ) + "),\n"

values_str = values_str[:-2] + ";"

table_name = "json_data"
sql_string = "INSERT INTO %s (%s)\nVALUES\n%s" % (
    table_name,
    ', '.join(columns),
    values_str
)

dbse.execute(sql_string)

dbse.execute("Select job_text, id_int, Bool, salary_float, name_string from json_data")
res = dbse.fetchall()

for r in res:
    print('Job:', r[0])
    print('Id in int:', r[1])
    print('Boolean:', r[2])
    print('Salary in float:', r[0])
    print('Name in String:', r[0])
    print()
