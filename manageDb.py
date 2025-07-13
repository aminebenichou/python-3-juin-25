import sqlite3

connect = sqlite3.connect("./db.sqlite3")

cursor = connect.cursor()

def createTable(table_name):
    cursor.execute(f""" 
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            desc TEXT,
            status TEXT  
        )
    """)
    connect.commit()

def addItemToTable(data, table_name):
    cursor.execute(f"""
            INSERT INTO {table_name} (title, desc, status)
            VALUES (?,?,?)
        """, (data['title'], '', 'not done')
    )
    connect.commit()