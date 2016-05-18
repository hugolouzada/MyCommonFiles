import os
import pickle

def getTableFromCache(queryStringWithoutSpace):
    try:
        return pickle.load(open(os.path.join("..","..","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"rb"))
    except:
        try:
            return pickle.load(open(os.path.join("..","..","..","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"rb"))
        except:
         try:
            return pickle.load(open(os.path.join("..","..","..","..","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"rb"))
         except:
            return pickle.load(open(os.path.join("..","..","..","..","..","ConnectToDatabase","Cache","Temp",queryStringWithoutSpace+".p"),"rb"))
