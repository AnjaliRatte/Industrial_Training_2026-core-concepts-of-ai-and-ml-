import os

data = os.listdir(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\Test")
# print(data)
for dr in data :
    path = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\Test",dr)
    images = os.listdir(path)
    print("number of images in " , dr , " are  :  ", len(images))