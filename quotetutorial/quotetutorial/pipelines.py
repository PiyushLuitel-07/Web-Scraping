# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class QuotetutorialPipeline:
   
    def __init__(self):
      self.create_connection()
      self.create_table()
    def create_connection(self):
      self.conn=mysql.connector.connect(
         host='localhost',
         user='root',
         passw='9803474343',
         database='myquotes'
      )
