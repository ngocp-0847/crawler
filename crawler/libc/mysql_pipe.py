import mysql.connector
from datetime import datetime
import json
from peewee import *
import os
import datetime

mydb = MySQLDatabase(
        os.getenv('MYSQL_DATABASE'),
        host = os.getenv('MYSQL_ENDPOINT'), 
        port = 3306,
        user = os.getenv('MYSQL_USERNAME'),
        passwd = os.getenv('MYSQL_PASSWORD'))

class BaseModel(Model):
    class Meta:
        database = mydb

class CrawlData(BaseModel):
    class Meta:
        table_name = 'crawl_data'
    domain = TextField()
    title = TextField()
    url = TextField()
    content = TextField()
    date = DateTimeField(default=None)
    created_at = DateTimeField(default=datetime.datetime.now)

mydb.connect()

class MysqlWriterPipeline(object):
    def open_spider(self, spider):
        print('open spider')

    def close_spider(self, spider):
        print('close spider')

    def process_item(self, item, spider):
        data = CrawlData(
            domain = item['domain'],
            title = item['title'],
            content = item['content'],
            url = item['url'],
            date = item['date'] if 'date' in item else None
        )
        # now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # sql = "INSERT INTO crawl_data (domain, title, url, content, created_at) VALUES (%s, %s, %s, %s, %s)"
        # val = (item['domain'], item['title'], item['url'], item['content'], now)
        if 'tags' in item:
            tagsstr = json.dumps(item['tags'])
            data['data'] = tagsstr
            # sql = "INSERT INTO crawl_data (domain, title, url, content, data, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
            # val = (item['domain'], item['title'], item['url'], item['content'], tagsstr, now)
        # if 'date' in item:
        #     datePublished = item['date'].strftime('%Y-%m-%d %H:%M:%S')
        #     sql = "INSERT INTO crawl_data (domain, title, url, content, data, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
        #     val = (item['domain'], item['title'], item['url'], item['content'], tagsstr, now)

        data.save()
        return item