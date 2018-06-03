import urllib.request
import sqlite3
import base64
import datetime
import sys
import argparse

def crawl_web(conn,url):
	print('creating Request and Header tables...')
	create_request_sql = 'create table if not exists Request(request_id INTEGER PRIMARY KEY AUTOINCREMENT,url TEXT,body TEXT,request_date TEXT)'
	create_header_sql = 'create table if not exists Header(request_id INTEGER,key TEXT,value TEXT,FOREIGN KEY(request_id) REFERENCES Request(request_id))'
	insert_request_sql = 'insert into Request(url,body,request_date) values(?,?,?)'
	insert_header_sql = 'insert into Header(request_id,key,value) values(?,?,?)'
	get_request_id_sql = "select seq from main.sqlite_sequence where name='Request'"
	conn.execute(create_request_sql)
	conn.execute(create_header_sql)
	print('crawling %s...' % (url))
	header_rows = []
	with urllib.request.urlopen(url) as response:
		html = response.read()
		headers = response.headers._headers
	print("inserting results into Request table")
	request_date = datetime.datetime.now().strftime('%Y%m%d')
	conn.execute(insert_request_sql,[url,html,request_date])
	cursor = conn.execute(get_request_id_sql)
	request_id = cursor.fetchone()[0]
	print("inserting results into Header table")
	header_rows = [(request_id,key,value) for key,value in headers]
	conn.executemany(insert_header_sql,header_rows)
	conn.commit()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Crawls url designated by url argument and puts url,header,body,and request date into sqlite database')
	parser.add_argument('url',nargs=1,help='URL to crawl')
	parser.add_argument('--db',default='crawler_db',help='sqlite database to store information from request')
	options = parser.parse_args()
	conn = sqlite3.connect(options.db)
	try:
		crawl_web(conn,options.url[0])
	finally:
		conn.close()