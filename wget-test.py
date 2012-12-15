#!/usr/bin/python2

import wget

if wget.wget("http://ipv4.download.thinkbroadband.com/5MB.zip") == 0:
    print "yo"



