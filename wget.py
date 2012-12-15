""" wget module
by Armin J. <netzverweigerer@gmail.com>

Will wget something...
Returns a tuple containing:
0) stdout 1) stderr 2) returncode
"""

__version__ = "0.1"

from subprocess import Popen, PIPE
import sys
import os


def wget(url):
    returncode = os.system('wget ' + url)
    return returncode

def wget2(url):
    p = Popen('wget ' + url, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    returncode = p.returncode
    if returncode == 0:
        print "wget: success. Output follows: "
        print "STDOUT: " + stdout
        print "STDERR: " + stderr
    else:
        print "wget: error. Returncode was: " + str(returncode)
        print "STDOUT: " + stdout
        print "STDERR: " + stderr


