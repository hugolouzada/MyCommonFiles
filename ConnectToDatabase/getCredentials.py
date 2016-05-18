import pandas as pd

def getCredentials():
    try:
        data = pd.read_csv('../../credentialsToDatabase.config', header = None)
    except:
        try:
            data = pd.read_csv('../credentialsToDatabase.config', header = None)
        except:
            data = pd.read_csv('credentialsToDatabase.config', header = None)
    return data

def getUserToDatabase():
    return getCredentials()[0][0]

def getPasswordToDatabase():
    return getCredentials()[0][1]

def getDatabaseName():
    return getCredentials()[0][2]