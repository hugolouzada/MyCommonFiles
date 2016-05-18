from isoweek import Week

def dateYYYY_MM_W(date):
    dayDate = date.day

    if dayDate<=8:
        weekNumber = 1
    elif dayDate<=16:
        weekNumber = 2
    elif dayDate<=23:
        weekNumber = 3
    else:
        weekNumber = 4

    return '%d-%02d(%1d)'%(date.year,date.month,weekNumber)

def dateYYYY_MM(date):
    return '%d-%02d'%(date.year,date.month)

def dateGrouping(df, ind, dateColumn):
    return dateYYYY_MM(df[dateColumn].loc[ind])

def dateWeekGrouping(df, ind, dateColumn="created_at"):
    return dateYYYY_MM_W(df[dateColumn].loc[ind])