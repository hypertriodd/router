import pexpect

R1='192.168.195.21'
UN='ciscouser'
PW='cisco.123'
DISPA='term len 0'
COMM1='conf t'
COMM2='int lo 0'
COMM3='ip add 1.1.1.1 255.255.255.255'
#Open Telnet
ssh='ssh -l ciscouser '+R1
t=pexpect.spawn(ssh)
t.expect('Password:')
t.sendline(PW)
t.expect('#')
#send command
t.sendline(DISPA)
t.expect('#')
t.sendline(COMM1)
t.expect('\(config\)#')
t.sendline(COMM2)
t.expect('\(config-if\)#')
t.sendline(COMM3)
t.expect('#')
#close telnet
t.sendline('end')
t.expect('#')
t.sendline('exit')
t.expect(pexpect.EOF)
