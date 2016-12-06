from commands import *
import sys

def run_command(cmd):
    print 'Running: "%s"' % cmd
    status, text = getstatusoutput(cmd)
    exit_code = status >> 8 # high byte
    signal_num = status % 256 # low byte
    print 'Status: x%04x' % status
    print 'Signal: x%02x (%d)' % (signal_num, signal_num)
    print 'Exit  : x%02x (%d)' % (exit_code, exit_code)
    print 'Core? : %s' % bool(signal_num & (1 << 8)) # high bit
    print 'Output:'
    print text
    print

run_command('git add .')
run_command('git commit -m '+ sys.argv[1]+'')
run_command('git push')
run_command('echo "LISTO"')
