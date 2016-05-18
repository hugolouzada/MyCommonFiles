def getWithTraceIfException(dic,item,Trace="-"):
    try:
        return dic[item]
    except:
        return Trace