import pandas as pd

def getPasswordToDatabase():
    try:
        data = pd.read_csv('../../credentialsToBivaDatabase.config', header = None)
    except:
        try:
            data = pd.read_csv('../credentialsToBivaDatabase.config', header = None)
        except:
            data = pd.read_csv('credentialsToBivaDatabase.config', header = None)
    return data[0][1]

# print(getPasswordToBivaDatabase())