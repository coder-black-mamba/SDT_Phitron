import os
import platform

if platform.system() == 'Windows':
    command = 'tasklist'
elif platform.system() == 'Darwin':  # Mac
    command = 'ps -ef'
else:  # Linux/Unix
    command = 'ps aux'

print(os.popen(command).read())