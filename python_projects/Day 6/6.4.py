#
# https://drive.google.com/file/d/1CZgeFoBc1xvFtOGER5QS5Rk1PRITjD5q/view
# get all files from a folder, and move to new, different folders where all .jpg file formats will be in the JPG named folder,
# .XML will be in the XML folder and PDF files will be in the PDF folder.

import os
import shutil

data = os.listdir(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\formats")
# print(data)

formats = []
for file in data :
    name,format = os.path.splitext(file)
    if format not in formats :
        formats.append(format)
# print(formats)

for f in formats :
    path = os.path.join(os.getcwd(),f)
    os.mkdir(path)

for f in formats :
    for file in data :
        if f in file :
            src = os.path.join(r"E:\PycharmProjects\Industrial_Training_2026\python_projects\Day 6\formats",file)
            dst = os.path.join(os.getcwd(),f)
            shutil.move(src,dst)


