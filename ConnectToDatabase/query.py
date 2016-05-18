import MySQLdb
import pandas as pd

from MyCommonFiles.ConnectToDatabase.Cache.getTableFromCache import getTableFromCache
from MyCommonFiles.ConnectToDatabase.Cache.saveTableOnCache import saveTableOnCache
from MyCommonFiles.ConnectToDatabase.getCredentials import getUserToDatabase, getPasswordToDatabase, getDatabaseName


def stringify(myString):

    tempString = myString.replace(' ','').replace('*','ALL').replace(',','_')
    return ''.join([x if x.isalnum() else '_' for x in tempString])


def query(query,getFromCache=False,queryName = None):
    if getFromCache:
        return getTableFromCache(stringify(query) if queryName==None else queryName)

    conn =  MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user=getUserToDatabase(),         # your username
                     passwd=getPasswordToDatabase(),  # your password
                     db=getDatabaseName())        # name of the data base

    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    df = pd.DataFrame(records)
    if len(df) != 0:
        df.columns = [desc[0] for desc in cursor.description]

    saveTableOnCache(df,stringify(query) if queryName==None else queryName)
    return df