import os, sys, time, string, subprocess

SFM_path = r"\Steam\steamapps\common\SourceFilmmaker\game"

for drive_letter in string.ascii_uppercase:
    if os.path.exists(drive_letter + r":\Program Files (x86)" + SFM_path):
        print("Found SFM on drive " + drive_letter)
        SFM_path = drive_letter + r":\Program Files (x86)" + SFM_path
        break
    if os.path.exists(drive_letter + r":" + SFM_path):
        print("Found SFM on drive " + drive_letter)
        SFM_path = drive_letter + r":" + SFM_path
        break
        
if SFM_path[0] == ":":
    input("ERROR: No SFM.exe found, press Enter to close")
    quit()
print("SFM path: "+SFM_path)

print("Scanning for existing .mdl files...")
old_mdls = []
for path, subdirs, files in os.walk(SFM_path+r"\workshop\models"):
    for name in files:
        if len(name) > 4 and name[-4:] == ".mdl":
            #print(os.path.join(path, name))
            old_mdls.append(name)

print(SFM_path+r"\SFM.exe")
SFM_exe_path = SFM_path+r"\SFM.exe"
subprocess.call(SFM_exe_path)

if not os.path.exists(os.getcwd()+"\\output\\"):
    os.mkdir("output\\")
for path, subdirs, files in os.walk(SFM_path+r"\workshop\models"):
    for name in files:
        if len(name) > 4 and name[-4:] == ".mdl" and name not in old_mdls:
            print("Found new model: ", name)
            subprocess.call([r"CrowbarCommandLineDecomp.exe", '-p', path+'\\'+name, '-o', os.getcwd()+"\\output\\"+name[:-4]])

input("Press Enter to close")