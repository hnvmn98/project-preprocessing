# -*- coding:utf-8 -*-
import csv

rf_dia = open('diagnose.csv','r')
dia_reader = csv.reader(rf_dia)
wf = open('combined.csv', 'w')
datawriter = csv.writer(wf)

coun = 0
for rlist_dia in dia_reader:
    coun += 1
    wlist = []
    for i in rlist_dia:
        wlist.append(i)
    rf_med = open('medical.csv', 'r')
    med_reader = csv.reader(rf_med)
    for rlist_med in med_reader:
        if ((rlist_med[0] == rlist_dia[1]) & (rlist_med[1] == rlist_dia[2])):
            print coun
            for j in rlist_med:
                wlist.append(j)
            break
    datawriter.writerow(wlist)
    rf_med.close()
rf_dia.close()
wf.close()
