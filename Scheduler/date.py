import time, datetime

now = datetime.datetime.now()
dt = datetime.datetime(2016, 05, 20, 04, 19, 0)
print now
while datetime.datetime.now() < dt:
    time.sleep(1)

print 'do work'