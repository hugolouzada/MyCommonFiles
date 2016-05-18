import pandas as pd

from MyCommonFiles.BASE_DIR_COMMON_FILES import BASE_DIR_COMMON_FILES


def getCredentials():
    return pd.read_csv(BASE_DIR_COMMON_FILES+'/credentialsToDatabaseConnection.config', header = None)

def getUserToDatabase():
    return getCredentials()[0][0]

def getPasswordToDatabase():
    return getCredentials()[0][1]

def getDatabaseName():
    return getCredentials()[0][2]