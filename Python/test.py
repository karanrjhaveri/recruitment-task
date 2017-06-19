import os, subprocess

cmd = []
cmd_size = 0
os.chdir('../data')
for line in open('cmd.txt','r'):
	cmd.append(line)
	cmd_size+=1
os.chdir('../Python')

for i in range(0,cmd_size):
	proc = subprocess.Popen(cmd[i], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	if((b'1000\r\n' == out) and (err is None)):
		print(cmd[i].replace('\n','') + ' --> Success')
	


