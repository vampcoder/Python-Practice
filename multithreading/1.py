import threading, time

print 'Start of Program'

def takeNap():
    time.sleep(2)
    print 'Wake Up'

threadObj = threading.Thread( target=takeNap)
threadObj.start()

print 'End'