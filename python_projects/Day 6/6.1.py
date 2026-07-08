import os


data= os.listdir(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\small images")

# print(data)

p = os.path.join(os.getcwd(),"newf") # os.getcwd gets current working directory
print(p)

os.mkdir(p)
import shutil
for img in data:
    src= os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\small images",img)
    # print(src)
    dst = os.path.join(p,img)
    # print(dst)
    shutil.copy(src,dst)