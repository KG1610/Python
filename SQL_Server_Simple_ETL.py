from plyer import notification
import pyodbc 
import pandas as pd
from UNPW import UN, PW

server = 'netstar-ssasgl' 
database = 'Reports' 
username = UN
password = PW

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

exportdataset = pd.read_sql_query("""
select top 2 *
from [Reports].[dbo].[Mystar]
""", cnxn)

exportdataset.to_excel(f'Exported_Data_FROM_{server}_{database}_Col_{exportdataset.shape[1]}_Row_{exportdataset.shape[0]}.xlsx', 
sheet_name='KG', startrow=5, startcol=5)

#Display Notitication to User
notification.notify(title=f"Python ETL from {server}", 
message= f"""
Data has been successfully Exported to csv - Super Awesome
Columns & Rows =  {exportdataset.shape}
Filename = Exported_Data_FROM_{server}_{database}_Col_{exportdataset.shape[1]}_Row_{exportdataset.shape[0]}.xlsx
""", 
timeout = 25)
