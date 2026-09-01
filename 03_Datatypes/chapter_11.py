# Advanced data types from collection
# Date, DateTime, Time, Calandar, TimeDelta(Delta means diffrence between two things)
# utilites Arrow, dateutil, 

import arrow

brewing_time = arrow.utcnow()
print(F"Brewing_utcTime {brewing_time}")
currnet_time = brewing_time.to("Asia/Calcutta")
print(F"Brewing_Europe {currnet_time}")

# from collections import namedtuple

