from datetime import datetime

from pandas.tseries.offsets import CustomBusinessDay

Holidays = [
    datetime(2015, 10, 12),
    datetime(2015, 11, 2),
    datetime(2015, 11, 20),
    datetime(2015, 12, 25),
    datetime(2016, 1, 1)
    ,datetime(2016, 1, 25)
    ,datetime(2016, 2, 8)
    ,datetime(2016, 2, 9)
    ,datetime(2016, 2, 10)
    ,datetime(2016, 3, 25)
]

bdayBrazil = CustomBusinessDay(holidays=Holidays)