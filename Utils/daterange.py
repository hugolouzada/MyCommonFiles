import datetime


def dateRange(startTuple,endTuple = None):
    if endTuple==None:
        endTuple = (datetime.datetime.today().year,datetime.datetime.today().month)

    drange = []
    for year in range(startTuple[0],endTuple[0]+1):
        for month in range(1,13):
            if (year == startTuple[0] and month >=startTuple[1]) or (year==endTuple[0] and month <= endTuple[1]) or (year>startTuple[0] and year<endTuple[0]):
              drange.append("%4d-%02d"%(year,month))
    return drange
