#!/bin/python

import sys

time = raw_input().strip()

h1,h2,c1,m1,m2,c2,s1,s2,c3,c4 = time


hour = int(h1+""+h2)
minute = int(m1+""+m2)
second = int(s1+""+s2)

morning = time.endswith("AM")
evening = time.endswith("PM")

if morning:
    if time == "12:00:00AM" :
        print "00:00:00"
    elif hour==12 :
        print "%02d:%02d:%02d"%(00,minute,second)
    else:
        print "%02d:%02d:%02d"%(hour,minute,second)


if evening:
    if time == "12:00:00PM" :
        print "12:00:00"
    elif hour==12 :
        print "%02d:%02d:%02d"%(hour,minute,second)
    else:
        print "%02d:%02d:%02d"%(hour+12,minute,second)
