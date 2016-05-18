import pandas as pd

def getUserToDatabase():
    try:
        data = pd.read_csv('../../credentialsToDatabase.config', header = None)
    except:
        try:
            data = pd.read_csv('../credentialsToDatabase.config', header = None)
        except:
            data = pd.read_csv('credentialsToDatabase.config', header = None)
    return data[0][0]

# print(getUserToDatabase())