import pexpect

R1='192.168.195.21' //IP Address Router
UN='ciscouser' // Username
PW='cisco.123' // Password
DISPA='term len 0' //disable paging
COMM1='conf t' // Enter Global Config
COMM2='int lo 0' //Interfaces
COMM3='ip add 1.1.1.1 255.255.255.255' //IP address
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
