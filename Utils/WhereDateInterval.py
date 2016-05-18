from datetime import date
from pandas.tslib import Timestamp



def WhereDateInterval(df, minDate, maxDate,dateTimeStampProperty="created_at"):

    maxDateDatetime = date(maxDate[0],maxDate[1],maxDate[2])
    minDateDatetime = date(minDate[0],minDate[1],minDate[2])

    return df.loc[(df[dateTimeStampProperty] < Timestamp(maxDateDatetime)) & (df[dateTimeStampProperty] >= Timestamp(minDateDatetime))]

