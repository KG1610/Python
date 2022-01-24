import sqlite3
import pandas as pd
from plyer import notification

# In memory database
#conn = sqlite3.connect(':memory:')

# Create DB file
# If exists will connect to DB
conn = sqlite3.connect('KG.db')
c = conn.cursor()


def createtable():
    # the three quotation marks "DOC STRING" allow us to write sql query on multiple lines
    c.execute("""
        create table if not exists Employee (
        First_Name text null,
        Last_Name text null,
        Position text null,
        Pay interger null
    )""")
    conn.commit


def insert():
    c.execute(
        """ 
        insert into Employee (First_Name, Last_Name, Position, Pay)
        values ('Kyle','Jardine','Python Developer', '180 000'), ('Lisa','Jardine','Hot Mamma House Wife', '0')
        """
    )
    conn.commit()
    print('Changes saved.')


def select():
    c.execute(""" select * from Employee """)
    conn.commit


def deleteall():
    c.execute("""
    delete from Employee
    """)
    conn.commit()
    print('Records from Employee Table Deleted')


createtable()
insert()
#deleteall()
#select()


def printselect():
    results = c.fetchall()
    for rows in results:
        print(rows)
#printselect()

sql_query_pd = pd.read_sql_query("""
                              select * from Employee 
                              """
                              ,conn)
print(sql_query_pd)
sql_query_pd.to_csv('Exported_Data.csv', index = False)
print(sql_query_pd.shape)

#for rows in sql_query_pd:
#    print(rows)

#Display Notitication to User
notification.notify(title="Status of Kyle's ETL Program", 
message= f"""
Data has been successfully Exported to csv
Columns =  {sql_query_pd.shape[1]}
Rows = {sql_query_pd.shape[0]}
""", 
timeout = 25)

conn.close
