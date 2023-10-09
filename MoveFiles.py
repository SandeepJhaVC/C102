import os
import shutil

fromDir = "C:/Users/Sandeep Jha/Downloads"
toDir = "D:/Sunny/Code/Downloaded"


list_of_files = os.listdir(fromDir)

for fileName in list_of_files:
    name,ext = os.path.splitext(fileName)
    
    if ext == "":
        continue
    if ext in [".pdf",".txt",".doc",".docx"]:
        path1 = fromDir + "/" + fileName
        path2 = toDir + "/" + "docFiles"
        path3 = toDir + "/" + "docFiles" + "/" + fileName

        if os.path.exists(path2):
            print("Moving.." + fileName)
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("Moving"+fileName)
            shutil.move(path1,path3)

##print(list_of_files)

