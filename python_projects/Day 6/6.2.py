# https://drive.google.com/file/d/1JSJyprt4OqHaFksmtIsB9fL47tGxkaRs/view
#
# create two folders Cat and Dog
#
# move cats photo in Cat folder and dogs in Dog

import os
import shutil

# "C:\Users\HP\Downloads\sample"
data = os.listdir(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\sample")
# print(data)

cat = os.path.join(os.getcwd(),"cats")
dog = os.path.join(os.getcwd(),"dogs")
os.mkdir(cat)
os.mkdir(dog)

for img in data :
    if "cat" in img :
        src = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\sample",img)
        dst = os.path.join(cat,img)
        shutil.move(src,dst)
    elif "dog" in img :
        src = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\sample", img)
        dst = os.path.join(dog, img)
        shutil.move(src, dst)