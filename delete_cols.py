# -*- coding:utf-8 -*-
import csv
import datetime
rf = open('combined.csv','r')
datareader = csv.reader(rf)
wf = open('result.csv', 'w')
datawriter = csv.writer(wf)

for rlist in datareader:
    if (rlist == []) | (rlist[11] != '0') | (rlist[6] == ''):
        continue
    #if rlist[10] != '1':
    #    continue
    wlist = []
    #wlist.append(rlist[1])
    wlist.append(rlist[37])
    date = datetime.datetime.strptime(rlist[6][:len(rlist[6]) - 8], "%Y/%m/%d")
    wlist.append(date.strftime("%Y%m%d")) #time
    #wlist.append(rlist[3])
    wlist.append(rlist[7])
    wlist.append(rlist[9]) #description
    #wlist.append(rlist[10])
    #wlist.append(rlist[11])
    #wlist.append(rlist[13])
    #wlist.append(rlist[25])
    #wlist.append(rlist[27])
    #wlist.append(rlist[28])
    #wlist.append(rlist[29])
    datawriter.writerow(wlist)

rf.close()
wf.close()
