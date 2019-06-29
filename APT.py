#!/usr/bin/env python3

import os, sys import win32print
import numpy

n = numpy.random.randint(4, high=9, size=None)
algorithms =   {1:"basic-counting-sort.txt", 2:"bucket-sort.txt",
                3:"counting-sort.txt", 4:"insertion-sort.txt",
                5:"quicksort.txt", 6:"radix-sort.txt",
                7:"selection-sort.txt", 8:"binary-search.txt",
                9:"breadth-first-search.txt", 10:"depth-first-search.txt"}

random_algorithm = numpy.random.randint(1, high=8, size=None)
random_algorithm_num = algorithms[random_algorithm]

#generate random array
array = numpy.random.randint(18, size=n)

#write random array to file
with open("algorithms/%s" % random_algorithm_num) as copy:
    with open('out.txt', 'w') as file:
        for line in copy:
            file.write(line)
        if random_algorithm_num != 9 or 10:
            file.write("\nn = %s" % n)
            file.write("\nArray = [")
            for i in range(0, n-1):
                file.write("%s, " % array[i])
            file.write("%s]\n" % array[n-1])
        else:
            file.write("reference example graphs")

#send page to printer
#printer name will need to be changed per network
os.system("lpr -P HP_LaserJet_MFP_M129_M134 out.txt")

#uncomment below, comment above, and revise printer name if on Windows
#p = win32print.OpenPrinter(printer_name)
#job = win32print.StartDocPrinter(p, 1, (out.txt, None, "RAW"))
#win32print.StartPagePrinter(p)
#win32print.WritePrinter(p, out.txt)
#win32print.EndPagePrinter(p)
