# Developer : Kyle Jardine
# Create Date: 2021-11-25
# Objective: Import AllSheets in Excel file into SQL Server each sheet as new table with the same name


import pyodbc
import pandas as pd
from sqlalchemy import create_engine, engine
from datetime import datetime
from plyer import notification
from UNPW import UN, PW

program_name = 'Import all sheets in an excel file to SQL'

Start_DateTime = datetime.now()

server = ''
database = ''
DRIVER = 'ODBC Driver 17 for SQL Server'
username = UN
password = PW
db_connection = f'mssql://{username}:{password}@{server}/{database}?driver={DRIVER}'

# create instance of the engine then create connection
engine = create_engine(db_connection)
DW_connection = engine.connect()

# list all drivers installed
for driver in pyodbc.drivers():
    # print(driver)
    if '.xlsx' in driver:
        mydriver = driver
# print(mydriver)

file_path = r'C:\Users\kylej\OneDrive - Altron Group\KAM_Fitment_Target_Import.xlsx'
#file_path = r'C:\Users\kylej\OneDrive - Altron Group\Python_WORK\SQL\Test_Import_2.xlsx'
#file_path = r'C:\Users\kylej\OneDrive - Altron Group\Python_WORK\Excel\Test_Workbook.xlsx'
#file_path= r'C:\Users\kylej\OneDrive - Altron Group\Python_WORK\SQL\Exported_Data_FROM_netstar-ssasgl_Reports_Col_29_Row_2.xlsx'

conn_str = (r'DRIVER={' + mydriver + '};'
            r'DBQ=' + file_path + ';'
            r'ReadOnly=0')

# print(conn_str)
cnxn = pyodbc.connect(conn_str, autocommit=True)
cursor = cnxn.cursor()

# get a list of all the sheets
tables = cursor.tables()
all_selects = []
table_list = []  # why couldnt I just use tables above? couldnt get it to work this way

for table in tables:
    # print(table[2])
    s = f'select * from [{table[2]}]'
    all_selects.append(s)
    table_list.append(table[2])

# print(all_selects)

# view all the data in Excel
# for query in all_selects:
#         e = cursor.execute(query)
#         for row in e:
#                 print(row)


# print(list(all_selects))
# for s in all_selects:
#     df = pd.read_sql_query(s, cnxn)
#     print(df)


# for t in table_list:
#     print(t[:-1])

for s, t in zip(all_selects, table_list):
    # print(s)
    # print(t[:-1])
    df = pd.read_sql_query(s, cnxn)
    df.to_sql(f'Python_Table_{t[:-1]}', DW_connection,
              if_exists='replace', index=False)

# for count, s in enumerate(all_selects):
#     print(count, s)
#     df = pd.read_sql_query(s, cnxn)
#     df.to_sql(f'Python_Table_{count}', DW_connection, if_exists='replace', index=False)

End_Datetime = datetime.now()
print(f'Start_DateTime: {Start_DateTime}')
print(f'Program: {program_name} \nStatus: Success \nStart DateTime: {Start_DateTime} \nDuration: {End_Datetime - Start_DateTime}')
print(f'{len(table_list)} Sheets inserted into new SQL Tables on {server}')

# Display Notitication to User
notification.notify(title=f'Program: {program_name}',
                    message=f"""
{len(table_list)} Sheets inserted into new SQL Tables on {server}
""",
                    timeout=25)
