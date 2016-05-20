import os
#s = os.mkdir('/root/PycharmProjects/Python Practice/Hello')
os.getcwd()
print os.path.relpath('/root/PycharmProjects/Python Practice' , '/root')
print os.path.dirname('/root/PycharmProjects/Python Practice')
print os.path.basename('/root/PycharmProjects/Python Practice')
print os.path.getsize('/root/PycharmProjects/Python Practice/FileIO/1.py')
dir = '/home/vampcoder/'
for i in os.listdir(dir):
    if os.path.isdir(os.path.join(dir, i)):
        print 'dir', i
        i = os.path.join(dir, i)
        print 'contents: '
        for j in os.listdir(i):
            str = j.rjust(40, '-')
            print str

    else:
        print 'file', i
