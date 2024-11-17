#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    #print t is number of test cases
    a = "3"
    number = int( a+(n-1)*"3")
    print "start number",number


    n_of_3 = str(number).count('3')
    n_of_5 = str(number).count('5')

    print "number of 3's",n_of_3
    print "number of 5's",n_of_5
    while( len(str(number)) == n):
        n_of_3 = str(number).count('3')
        n_of_5 = str(number).count('5')

        if (n == n_of_5 + n_of_3) and (n_of_3 % 5 == 0) and (n_of_5 % 3 == 0) :
            print "sir yes sir",number
        number +=1
