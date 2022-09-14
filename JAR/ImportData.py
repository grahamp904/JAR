import pandas as pd
import pyodbc
import sqlalchemy as sa
from sqlalchemy.engine import URL
from sqlalchemy.types import NVARCHAR




def Import_CSV(fpath,fname,tname):
  file_csv = fpath + fname
  data = pd.read_csv(file_csv, low_memory=False)
   
  server = "localhost\SQLEXPRESS01"
  database = 'JAR'
  
  connection_string  = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=True'
  connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

  engine = sa.create_engine(connection_url)
  data.to_sql(tname, engine, if_exists='replace')
    
   
def Import_MBD (fpath,fname,tname):
  file_mdb = fpath + fname
   
  server = "localhost\SQLEXPRESS01"
  database = 'JAR'
  conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+file_mdb+';')
  SQL_Query = pd.read_sql('''Select * from ParcelView''', conn)

  connection_string  = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=True'
  connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

  engine = sa.create_engine(connection_url)
  SQL_Query.to_sql(tname, engine, if_exists='replace')