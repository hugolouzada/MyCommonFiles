def pairSortedByKey(dic):
        return [(x, dic[x]) for x in sorted(dic.keys())]
