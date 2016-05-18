import psycopg2
import pandas as pd

from ConnectToDatabase.Cache.getTableFromCache import getTableFromCache
from ConnectToDatabase.Cache.saveTableOnCache import saveTableOnCache
from ConnectToDatabase.getPasswordToDatabase import getPasswordToDatabase
from ConnectToDatabase.getUserToDatabase import getUserToDatabase

def stringify(myString):

    tempString = myString.replace(' ','').replace('*','ALL').replace(',','_')
    return ''.join([x if x.isalnum() else '_' for x in tempString])

def query(query,getFromCache=False,queryName = None):
    if getFromCache:
        return getTableFromCache(stringify(query) if queryName==None else queryName)

    user = getUserToDatabase()
    password = getPasswordToDatabase()
    conn_string = "dbname=%s host=%s user=%s password=%s" % (
    "db_name", "myhost", user, password)

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    df = pd.DataFrame(records)
    if len(df) != 0:
        df.columns = [desc[0] for desc in cursor.description]

    saveTableOnCache(df,stringify(query) if queryName==None else queryName)
    return df