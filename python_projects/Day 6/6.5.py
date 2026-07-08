# https://drive.google.com/file/d/1APyqWFBL3ZZ9nebLH6K-ove43-hAvYar/view?usp=sharing
#
# n02085620_1073.jpg each file name is different we have to check after underscore
# number is even or odd if even move to even named folder else in odd
import os
import shutil

data = os.listdir(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\data")
print(data)
odd = os.path.join(os.getcwd(),"odd")
even = os.path.join(os.getcwd(), "even")

os.mkdir(odd)
os.mkdir(even)

for i in range(1,len(data)):
    file = data[i]
    num = file.split("_")[1].split(".")[0]
    if int(num)%2 == 0 :
        src = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\data",file)
        dst = os.path.join(even,file)
        shutil.move(src,dst)
    else :
        src = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\data", file)
        dst = os.path.join(odd, file)
        shutil.move(src, dst)


