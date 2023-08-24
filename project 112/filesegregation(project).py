import os
import shutil

from_dir = "C:/Users/HP/Downloads"
to_dir = "D:/whjr/class 112"


list_of_files=os.listdir(from_dir)
#print(list_of_files)

for filename in list_of_files:
    name,ext = os.path.splitext(filename)
    #print(name)
    #print(ext)

    if ext == " ":
        continue
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+filename
        path2 = to_dir+"/"+"images"
        path3 = to_dir+"/"+"images"+"/"+filename

        #print(path1)
        #print(path2)
        #print(path3)

        if os.path.exists(path2):
            print("moving the files")
            shutil.move(path1,path3)
        
        else:
            print("creating the path")
            os.makedirs(path2)
            print("moving the files")
            shutil.move(path1,path3)