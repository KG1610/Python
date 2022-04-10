import pandas as pd
from UNPW import UN, PW, CRM_username, CRM_password
from sqlalchemy import create_engine, engine
from CRM_Query import CRM_QUERY
from datetime import datetime
from datetime import date
import datacompy as dc 

Start_DateTime = datetime.now()
print(f'Start_DateTime {Start_DateTime}')

#Database Connection Variables for both source and target
SERVER = 'Netstar-SSASGL' 
DATABASE = 'Reports' 
DRIVER = 'ODBC Driver 17 for SQL Server'
USERNAME = UN
PASSWORD = PW
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

 

engine = create_engine(DATABASE_CONNECTION)
DW_connection = engine.connect()

#use Pandas to execute query and then create dataframe
Query_StartTime = datetime.now()
print(f'starting CRM Query {Query_StartTime}')
crm_query = pd.read_sql_query("""
select *, convert(varchar, [Opportunity_Reference]) + '|' + isnull(convert(varchar(50),  [Parent_Contract_Line_ID]), convert(varchar, '')) as 'python_Key'
  FROM [Netstar_DW].[dbo].[Sales_Riaan]
""", DW_connection)
Query_EndTime = datetime.now()
print(f'CRM Query Finished Executing: {Query_EndTime - Query_StartTime}')

df_CRM = pd.DataFrame(crm_query)
print(df_CRM.shape)

#Now we get the DW query into a dataframe
DW_Query_starttime = datetime.now()
print(f'Starting DW Query {DW_Query_starttime}')
dw_query = pd.read_sql_query('select * from Netstar_DW.dbo.Riaan_Sales_Proc', DW_connection)
DW_Query_EndTime = datetime.now()
print(f'DW Query Finished Executing: {DW_Query_EndTime - DW_Query_starttime}')


df_DW = pd.DataFrame(dw_query)
print(df_DW.shape)

Compare_Starttime = datetime.now()
print(f'Starting Query Comparison {Compare_Starttime}')

compare = dc.Compare(
    df_CRM, 
    df_DW,
    join_columns = 'python_Key',  #You can also specify a list of columns eg ['policyID','statecode']
    abs_tol = 0, #Optional, defaults to 0
    rel_tol = 0, #Optional, defaults to 0
    df1_name = 'CRM', #Optional, defaults to 'df1'
    df2_name = 'DW' #Optional, defaults to 'df2'
)
print(compare.report())

date = date.today()
# export_path = 'C:\Users\kylej\OneDrive - Altron Group\git_python\Python\Items_not_to_sync'
with open(f"Python_data_comparison_v3_{date}.txt", "w", encoding="utf-8") as f:
    f.write(compare.report())
    f.close()

P_endtime = datetime.now()
print(f'Program Completed: {P_endtime - Start_DateTime}')

