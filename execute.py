""" execute

Armin J. <netzverweigerer@gmail.com>

Will execute shell commands.
Returns a tuple containing:
0) stdout 1) stderr 2) returncode

Example usage to get the returncode:

from Execution import Executor
e = Executor('yourcommand --some-args foo')
e.run()
print e.tup[2]

"""

__version__ = "0.1"

from subprocess import Popen, PIPE
import sys

class execute(object):
    def __init__(self,cmd):
        self.cmd = cmd
        self.run()
    def run(self):
        p = Popen(self.cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.stdout, self.stderr = p.communicate()
        self.returncode = p.returncode
        self.tup = self.stdout, self.stderr, self.returncode

if __name__ == '__main__':
    print("This script is intended to run as a module.")
    sys.exit(1)

