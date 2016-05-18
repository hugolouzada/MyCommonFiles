import os
import pickle

from MyCommonFiles.BASE_DIR_COMMON_FILES import BASE_DIR_COMMON_FILES

def getTableFromCache(queryStringWithoutSpace):
    return pickle.load(open(os.path.join(BASE_DIR_COMMON_FILES,"MyCommonFiles","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"rb"))
