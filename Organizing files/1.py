import shutil, os, send2trash, time

#shutil.copy('../FileIO/1.py', 'text.py')
#shutil.copytree('../FileIO/', 'FileIO')
#shutil.move('text.py', '../FileIO/')

os.mkdir('Hello')
os.mkdir('FileIO')
time.sleep(1)
send2trash.send2trash('./Hello')
send2trash.send2trash('./FileIO')