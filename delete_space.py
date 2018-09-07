# -*- coding:utf-8 -*-
import csv

rf = open('input.csv','r')
reader = csv.reader(rf)
wf = open('test.csv', 'w')
datawriter = csv.writer(wf)
coun = 0
coun_stop = 0
for rlist in reader:
    coun = coun + 1
    if coun == 154:
        count_stop = 1
    wlist = []
    for i in rlist:
        tuple_str = ''
        for j in i:
            if j != ' ':
                tuple_str += j
        wlist.append(tuple_str)
    datawriter.writerow(wlist)

rf.close()
wf.close()
