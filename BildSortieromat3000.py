import os, sys

# here goes file path:
filepath = "/Users/nilsvanburk/Pictures/Bildschirmfotos/PythonTest"
platzhalter = "placeholder"
# here goes file extension:
fileextension = ".png"

filelist=sorted(os.listdir(filepath))
# print(filelist)

temp_filelist=[]

for element in filelist:
    if fileextension in element:
        temp_filelist.append(element)

if len(filelist) >999:
    print("WARNING! More than 999 files in "+filepath+"!")
    sys.exit()

for i in range(len(temp_filelist)):
    # print(platzhalter+"_"+"{:03d}".format(i+1))
    file=filepath+"/"+temp_filelist[i]
    # here goes: instead of "platzhalter" new filename / beachte: # {:04d} for 1000-9999 files!
    newfile=filepath+"/"+platzhalter+"_"+"{:03d}".format(i+1)+fileextension
    # print(file)
    os.rename(file, newfile)
