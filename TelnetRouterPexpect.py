import pexpect

R1='192.168.195.21'
UN='ciscouser'
PW='cisco.123'
DISPA='term len 0'
COMM='show run'
#Open Telnet
ssh='ssh -l ciscouser '+R1
t=pexpect.spawn(ssh)
t.expect('Password:')
t.sendline(PW)
t.expect('#')
#send command
t.sendline(DISPA)
t.expect('#')
t.sendline(COMM)
t.expect('#')
data=t.before
#close telnet
t.sendline('exit')
t.expect(pexpect.EOF)
#Opening File
f=open('router output','w')
f.write(data)
f.close()