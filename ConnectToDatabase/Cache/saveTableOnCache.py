import os
import pickle

from MyCommonFiles.BASE_DIR_COMMON_FILES import BASE_DIR_COMMON_FILES


def saveTableOnCache(table,queryStringWithoutSpace):
	file = open(os.path.join(BASE_DIR_COMMON_FILES,"MyCommonFiles","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"wb")
	return pickle.dump(table,file)