def pairSortedByValue(dic,rev=False):
        return [(x, dic[x]) for x in sorted(dic,key=dic.get,reverse=rev)]
