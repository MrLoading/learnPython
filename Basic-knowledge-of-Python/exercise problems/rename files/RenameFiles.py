# -*- coding: utf-8 -*-
import os

print(os.getcwd())

# os.chdir('./Unsorted')

for f in os.listdir('./Unsorted'):

    # split off the extension from the file name
    f_name, f_ext = os.path.splitext(f)

    # get the title, course, number by doing a split on the f_name
    f_title, f_course, f_num = f_name.split('-')

    # strip away any white space that is on the left and right
    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_num = f_num.strip()

    # f_num = f_num.strip()[1:]  # grabbing everything from second character on

    # pad the single digits (like 1,10 ->01, 10) with zeros
    f_num = f_num.strip()[1:].zfill(2)

    # print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
    # print('{}-{}{}'.format(f_num, f_title, f_ext))

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename('./Unsorted/' + f, './Sorted/' + new_name)
