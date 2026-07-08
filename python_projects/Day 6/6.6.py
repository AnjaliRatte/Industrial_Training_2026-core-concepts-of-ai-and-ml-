# https://drive.google.com/file/d/1Z-3nFm6FjSM5KyZTgGOyFGuYQPYMwpmZ/view
#
# Move all folders in the new folders folder name, and image names should be like
#
# Apple Braeburn
#      Apple Braeburn_1.jpg
#      Apple Braeburn_1.jpg
#
# Banana
#      Banana_1.jpg
#      Banana_2.jpg

import os
import shutil

data = os.listdir(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\Test")
for folder in data :
    path = os.path.join(os.getcwd(),folder)
    os.mkdir(path)
    name = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\Test", folder)
    files = os.listdir(name)
    for i in range(len(files)):
        new_name = folder + "_" + str(i) + ".jpg"
        src = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\Test",folder,files[i])
        dst = os.path.join(os.getcwd(), folder ,new_name )
        shutil.move(src,dst)

