#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, Error

# import Python's built-in JSON library
import json

# import the JSON library from psycopg2.extras
from psycopg2.extras import Json

# import psycopg2's 'json' using an alias
from psycopg2.extras import json as psycop_json

# import Python's 'sys' library
import sys

# accept command line arguments for the Postgres table name
if len(sys.argv) > 1:
    table_name = '_'.join(sys.argv[1:])
else:
    # ..otherwise revert to a default table name
    table_name = "newtable"

print ("\ntable name for JSON data:", table_name)


# Json data 가져오기
with open('SiteUsageDetails_20210716T0849038637.json', encoding='UTF8') as json_data:

    # use load() rather than loads() for JSON files
    record_list = json.load(json_data)

# print ("\nrecords:", record_list)
# print ("\nJSON records object type:", type(record_list)) # should return "<class 'list'>"



sql_string = 'INSERT INTO {} '.format( table_name )

# if record list then get column names from first key
if type(record_list) == list:
    first_record = record_list[0]

    # key 값 / columns 값
    columns = list(first_record.keys())
    print ("\ncolumn names:", columns)

# if just one dict obj or nested JSON dict
else:
    print ("Needs to be an array of JSON objects")
    sys.exit()
# print(len(columns))

# 추가작업 - 특수문자로 인한 컬럼값 변경
columns[0] = 'odata_type'
# print(columns)


# enclose the column names within parenthesis
sql_string += "(" + ', '.join(columns) + ")\nVALUES "

# print(sql_string)


# enumerate over the record
for i, record_dict in enumerate(record_list):

    # iterate over the values of each record dict object
    values = []
    for col_names, val in record_dict.items():
        # if val == None:
        #     val == 'NULL'
        #     print(val)
        # Postgres strings must be enclosed with single quotes
        if type(val) == str:
            # escape apostrophies with two single quotations
            val = val.replace("'", "''")
            val = "'" + val + "'"

        values += [ str(val) ]

    # join the list of values and enclose record in parenthesis
    sql_string += "(" + ', '.join(values) + "),\n"
    break
# print(sql_string[0:10])
# # remove the last comma and end statement with a semicolon
sql_string = sql_string[:-2] + ";"

# print ("\nSQL string:")
print (sql_string)




# 데이터 import 부분

import psycopg2 # driver 임포트

conn = psycopg2.connect(host='localhost', dbname='postgres',user='postgres',password='1234',port=5432)


cur = conn.cursor() # 커서를 생성한다


cur.execute(sql_string) # WRONG
