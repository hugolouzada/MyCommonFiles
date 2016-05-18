import os
import pickle

def saveTableOnCache(table,queryStringWithoutSpace):
	file = open(os.path.join("..","MyCommonFiles","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"wb")
	return pickle.dump(table,file)