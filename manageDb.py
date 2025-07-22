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


def retrieveItems():
    tasks = cursor.execute("""
        SELECT * FROM tasks
    """).fetchall()
    print(tasks)
    return tasks

def deleteItemFromDb(id):
    cursor.execute(f"""
        DELETE FROM tasks WHERE id={id}
    """)

    connect.commit()


def updateItem(status, id):
    cursor.execute(f"""UPDATE tasks SET status = '{status}' WHERE id={id} """)
    connect.commit()