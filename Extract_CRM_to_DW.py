import pandas as pd
from UNPW import UN, PW, CRM_username, CRM_password
from sqlalchemy import create_engine, engine
from CRM_Query import CRM_QUERY
from datetime import datetime
 

Start_DateTime = datetime.now()
print(f'Start_DateTime {Start_DateTime}')

#Database Connection Variables for both source and target
SERVER = '' 
DATABASE = '' 
DRIVER = 'ODBC Driver 17 for SQL Server'
USERNAME = UN
PASSWORD = PW
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

CRM_server = '' 
CRM_database = '' 
CRM_username = CRM_username
CRM_password = CRM_password
CRM_DRIVER = 'ODBC Driver 17 for SQL Server'
CRM_DATABASE_CONNECTION = f'mssql://{CRM_username}:{CRM_password}@{CRM_server}/{CRM_database}?driver={CRM_DRIVER}'

#create instance of the engine then create connection 
CRM_engine = create_engine(CRM_DATABASE_CONNECTION)
CRM_connection = CRM_engine.connect()

engine = create_engine(DATABASE_CONNECTION)
DW_connection = engine.connect()

#use Pandas to execute query and then create dataframe
Query_StartTime = datetime.now()
print(f'starting Query {Query_StartTime}')
crm_query = pd.read_sql_query(CRM_QUERY, CRM_connection)
Query_EndTime = datetime.now()
print(f'Query Finished Executing: {Query_EndTime - Query_StartTime}')

df_CRM = pd.DataFrame(crm_query)
print(df_CRM.shape)

#use pandas to insert into DW
Insert_Startime = datetime.now()
print(f'Inserting into DW : {Insert_Startime}')
df_CRM.to_sql('Python_CRM_QUERY', DW_connection, if_exists='replace', index=False)
Insert_Endime = datetime.now()
print(f'ETL completed {Insert_Endime - Insert_Startime}')