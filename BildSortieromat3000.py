# program capable of renaming all files of the same type within a folder in ascending order:
import os, sys
# insert file path here:
filepath = "/Users/nilsvanburk/Pictures/Bildschirmfotos/PythonTest"
platzhalter = "Bildschirmfoto"
# filter by file extension here:
fileextension = ".png"

filelist=sorted(os.listdir(filepath))
# optionally check the sorted list:
# print(filelist)

temp_filelist=[]

for element in filelist:
    if fileextension in element:
        temp_filelist.append(element)

if len(filelist) >999:
    print("WARNING! More than 999 files in " + filepath + "!")
    sys.exit()

for i in range(len(temp_filelist)):
    # optionally check the renaming scheme first:
    # print(platzhalter + "_" + "{:03d}".format(i+1))
    file = filepath + "/" + temp_filelist[i]
    # note: {:04d} for 1000-9999 files!
    newfile = filepath + "/" + platzhalter + "_" + "{:03d}".format(i+1)+fileextension
    # optionally check the renamed file list before actually renaming:
    # print(file)
    os.rename(file, newfile)
