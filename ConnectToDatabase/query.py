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

    df = pd.read_sql(query, con=conn)

    saveTableOnCache(df,stringify(query) if queryName==None else queryName)
    return df