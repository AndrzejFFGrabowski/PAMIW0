from flask import make_response, render_template
import sqlite3
from sqlite3 import Error

def generateSqlSite():
    create_connection("pythonDB.db",""" CREATE TABLE IF NOT EXISTS products (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """)
    return render_template("sql.html")

def fuc():
    return "yes"
    



def create_connection(db_file,sql):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print("it's alive")
        print(sql)
    except Error as e:
        print(e)
    finally:
        if conn:
            msg=executeSql(conn,sql)
            print(executeSql(conn,"SELECT * FROM products;"))
            conn.close()
            return msg


def addProductToDB():
    create_connection("pythonDB.db",""" INSERT INTO products
                                        (id, name)
                                        VALUES
                                        (1, "strawbery")""")
    return generateSqlSite()
                                    
def showProducts():
    msg=create_connection("pythonDB.db","""SELECT * FROM products;""")
    text=""
    for row in msg:
    	text=text+row
    return text
    
def executeSql(conn, sql):
    try:
    	c = conn.cursor()
    	c.execute(sql)
    	msg=c.fetchall()
    	return msg
    except Error as e:
    	print(e)
    	return "Server Error 501"
    	
    
