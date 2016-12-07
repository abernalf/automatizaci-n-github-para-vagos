from commands import *
import sys

def run_command(cmd):
    print 'Running: "%s"' % cmd
    status, text = getstatusoutput(cmd)
    exit_code = status >> 8 
    signal_num = status % 256 
    print 'Status: x%04x' % status
    print 'Signal: x%02x (%d)' % (signal_num, signal_num)
    print 'Exit  : x%02x (%d)' % (exit_code, exit_code)
    print 'Core? : %s' % bool(signal_num & (1 << 8)) 
    print 'Output:'
    print text
    print
volcado = sys.argv
commit = ''
ind = 1
tam = len(volcado)
for i in range (1,tam):
    volcado[ind]
    commit = commit +' '+volcado[ind]
    ind = ind +1;


run_command('git add .')
run_command('git commit -m "'+ commit+'"')
run_command('git push')
run_command('echo "LISTO"')
