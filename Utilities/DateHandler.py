import time
import datetime

# ********************************************
# Date
t = time

# 20190828
today_YYYYMMDD = t.strftime('%Y%m%d')

# 28/08/2019
today_DD_MM_YYYY = t.strftime("%d/%m/%Y")

# ********************************************
# Hour
h = datetime.datetime.now()

# HourMinutes - 1128
hour_HHMM = str(h.hour) + str(h.minute )

# HourMinutesSeconds - 112830
hour_HHMMSS = str(h.hour) + str(h.minute) + str(h.second)