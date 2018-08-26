'''
Created on Aug 26, 2018

@author: teryx
'''
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlalchemy
import db
from sqlalchemy import Table, Column, String, MetaData
import pandas as pd

import common

logger = common.get_logger(__name__)

def main():
    
#     create_db(db.DB_NAME)
    create_table('journals', db.JOURNALS_SQL)

def get_engine(user=db.USER, password=db.PASSWORD, port=db.PORT, db_name=db.DB_NAME):
    
    engine = sqlalchemy.create_engine(db.CONNECTION_STRING.format(user, password, port, db_name))
    
    return engine

def get_conn(user=db.USER, password=db.PASSWORD, port=db.PORT, db_name=db.DB_NAME):
    
    engine = sqlalchemy.create_engine(db.CONNECTION_STRING.format(user, password, port, db_name))
    conn = engine.connect()
    
    return conn

def write_df(table_name, df):
    
    #TODO: add time logs
    df.to_sql(table_name, get_engine(), if_exists='append', index=False)
    logger.info('Inserted {} rows to {}.{}'.format(df.shape[0], db.DB_NAME, table_name))

def create_db(new_db_name):    
    
    conn = get_conn(db_name=db.DEFAULT_DB_NAME)
    conn.execute('commit')
    conn.execute('create database {}'.format(new_db_name))
    conn.close()
    #https://stackoverflow.com/questions/6506578/how-to-create-a-new-database-using-sqlalchemy
    
    logger.info('DB {} created.'.format(new_db_name))
    
def create_table(new_table_name, sql_string):
    
    conn = get_conn()
    conn.execute(sql_string)
    conn.close()
    #https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
    
    logger.info('DB {} created.'.format(new_table_name))

if __name__=='__main__':
    main()