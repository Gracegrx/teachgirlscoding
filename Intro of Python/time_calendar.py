import time
import calendar
print time.time()
print time.localtime(time.time())
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

print calendar.month(2017, 7)