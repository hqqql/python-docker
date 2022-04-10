import psycopg2
import json
from flask import Flask
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/test')
def test():
    return 'good'

@app.route('/createdb')
def db_create():
    database = "postgres"
    user = "postgres"
    pwd = "123456"
    host = "postgres_container"
    port = 5432
    db_name = "testdb"
    try:
        conn = psycopg2.connect(database=database, user=user, password=pwd, host=host, port=port)
    except:
        return 'failed to connect'


    # 创建数据库
    try:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("drop database if exists %s"%db_name)
        cur.execute("CREATE DATABASE %s"%db_name)
    except:
        conn.commit()
        conn.close()
        return 'failed to createDB'

    conn.commit()
    conn.close()
    return "Create database successfully"

@app.route('/initdb')
def db_init():
    db_create()
    database = "testdb"
    user = "postgres"
    pwd = "123456"
    host = "postgres_container"
    port = 5432
    try:
        conn = psycopg2.connect(database=database, user=user, password=pwd, host=host, port=port)
    except:
        return 'failed to connect'

    cur = conn.cursor()
    try:
        cur.execute('drop table if exists student')
        cur.execute('''CREATE TABLE student (
           ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL);''')
    except:
        conn.commit()
        conn.close()
        return 'create table failed'

    try:
        cur.execute("INSERT INTO student (ID,NAME) VALUES (1, 'Paul')")
        cur.execute("INSERT INTO student (ID,NAME) VALUES (2, 'Bob')")
        cur.execute("INSERT INTO student (ID,NAME) VALUES (3, 'Jock')")
    except:
        conn.commit()
        conn.close()
        return 'insert failed'
    conn.commit()
    conn.close()
    return 'init database'
