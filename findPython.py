# version 1.0.2
# script to recursively find all files with .py extension 
# starting from the directory and its subs from where the script
# is executed. The process writes each file/path found.
# example, if executed from `scripts`, the  first path list any in 
# the scripts/ dir, then recurses myPython/ sub.
# ie. [PosixPath('findPython.py'), PosixPath('scripts/myPython/tryPython.py'),..]
#
# BE ADVISED: when executed from HOME (Users/{RACF}), this scans all 
# user space directories! On mac, that includes ~/Library/Application Support. 
#
# Useage: python findPythin.py
# NOTE - Confirm HOME points to users RACF-ID directory
#
# Windows User Example:
# PS C:\Users\{RACF}\{Subdir}> python findPython.py
#
# Mac User Example:
# \Users\{RACF}\{Subdir}$ python findPython.py
#
import os
import csv
from pathlib import Path

"""
set the parent directory from the directory (and decendents) where
the command is executed. If the abosute path to the parent
dir is /Users/RACF/myPython, then '.' would be myPython.
"""
p = Path('.')
csvPath = os.environ.get("HOME") + "/Documents/"
csvFile = "python.pyp.csv"
print("csv file: " + csvPath + csvFile)


"""
returns list of path/file.py
ex. ['./myRoot.py', './subPyRes/resPy.py',...]
"""
def pyList(p):
  file_list = []
  for root, _, files in os.walk(p):
    for filename in files:
      path = os.path.join(root, filename)
      if os.path.isfile(path):
        _, ex = os.path.splitext(path)
        if ex == ".py":
          file_list.append(path)
  return file_list


"""
write .py files in List to csv text file.
path/file reference is from executed parent directory
ex. if parent is myPython/ with sub dir lib/,
    the path/file would be ./lib/myMain.py 
"""
def writePyPath(fileList, csvPath, csvFile):
  csvOut = csvPath + csvFile
  with open(csvOut, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for fileStr in fileList:
      writer.writerow([fileStr])
  # print("done writing files to csv " + csvOut)


"""
reads in each path/file and removes it if the file exist.
NOTE: process is atomic!  confirm removed in csv file list.
ex. if ./lib/myMain.py is included in the csv file, the abs path is 
    /Users/RACF/myPython/lib/myMain.py when executed from myPython parent.
"""
def readRemovePy(csvPath, csvFile):
  try:
    path = csvPath + csvFile
    with open(path, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        fname = row[0].strip() # file names in each row
        print(f"removing: {fname}")
        if os.path.exists(fname):
          os.remove(fname)
        else:
          print(f"{fname} is not a file moving on to next...")

  except FileNotFoundError:
    print(f"Error: CSV file not found at {fname}")

  except Exception as e:
    print(f"Unexpected error: {e}")



fileList = pyList(p)
_ = writePyPath(fileList, csvPath, csvFile)
_ = readRemovePy(csvPath, csvFile)
print(f"done removing files! See removed in {csvPath + csvFile}")

