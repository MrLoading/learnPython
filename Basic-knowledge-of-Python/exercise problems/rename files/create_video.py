# -*- coding: utf-8 -*-
with open('video_name_list.txt', 'r') as f:
    rline = f.readline()
    while len(rline) > 0:
        fname = rline.split('\n')
        tmp = open('./Unsorted/' + fname[0], 'w+')
        tmp.write(rline)
        tmp.close()
        print("create file : ", rline)
        rline = f.readline()
