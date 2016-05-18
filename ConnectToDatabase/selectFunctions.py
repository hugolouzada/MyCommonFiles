from MyCommonFiles.ConnectToDatabase.query import query


def selectAll(table, getFromCache=False):
    queryString = "SELECT * FROM %s" % (table)
    return query(queryString,getFromCache)


def selectOneColumn(column, table, getFromCache=False):
    queryString = "SELECT %s FROM %s" % (column,table)
    return query(queryString,getFromCache)

def selectMultipleColumns(columns, table, getFromCache=False):
    columsSQLFormat = ', '.join(columns)
    queryString = "SELECT %s FROM %s" % (columsSQLFormat,table)
    return query(queryString,getFromCache)