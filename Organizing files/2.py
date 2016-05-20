import os

i = 1

path = '/root/PycharmProjects'

for folderName, subFolders, fileNames in os.walk(path):
    print 'The current folder is ', folderName

    for subfolder in subFolders:
        print '==', subfolder
    for filename in fileNames:
        print '--', filename

    print ' '