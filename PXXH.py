import sqlite3
import base64
import argparse

def retrieve_header_information(conn,request_id):
	header_sql = "select key,value from Header where request_id=?"
	cursor = conn.execute(header_sql,[request_id])
	for row in cursor:
		print("KEY:{key} VALUE:{value}".format(key=row[0],value=row[1]))
def retrieve_request_information(conn,timestamp):
	request_sql = "select request_id,url,body from request where request_date=?"
	cursor = conn.execute(request_sql,[timestamp])
	print("Retrieving requests for %s..." % timestamp)
	for row in cursor:
		print("URL")
		print(row[1])
		print
		print("HEADERS")
		retrieve_header_information(conn,row[0])
		print
		print("BODY")
		print(row[2])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Takes timestamp as imput and returns request url,header,and body info from sqlite database')
	parser.add_argument('timestamp',nargs=1,help='timestamp in format YYYYMMDD')
	parser.add_argument('--db',default='crawler_db',help='sqlite database to store information from request')
	options = parser.parse_args()
	conn = sqlite3.connect(options.db)
	try:
		retrieve_request_information(conn,options.timestamp[0])
	finally:
		conn.close()