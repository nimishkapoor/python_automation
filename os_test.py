import os
from datetime import datetime
#print(dir(os))
print(os.getcwd())
os.chdir('/Users/nimishkapoor/Downloads')
print(os.getcwd())
#print(os.listdir(os.getcwd()))
#os.mkdir('new_folder_')
#os.makedirs('new_folder_1/new_folder_2')

#os.rmdir('new_folder_')
#os.removedirs('new_folder_1/new_folder_2')
#os.rename('watch.html','demo.txt')
#print(os.stat('demo.txt'))
#print(os.stat('demo.txt').st_size)

#mod_time=os.stat('demo.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))

#for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#	print('Current Path:', dirpath)
#	print('Directories:',dirnames)
#	print('Files:',filenames)

print(os.environ.get('HOME'))
file_path=os.path.join(os.environ.get('HOME') , 'test.txt')
print(file_path)
print(os.path.basename(file_path))
print(os.path.dirname(file_path))
print(os.path.split(file_path))


print(os.path.exists(file_path))
#with open(file_path, 'w') as f:
#	f.write

os.system("pwd")