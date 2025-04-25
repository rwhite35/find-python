## findPython.py ##
- Version: 1.0.2
- Since: 20250424

### TESTING PYTHON FILE STRUCTURE ###

Project includes `testPyPath` with mixed file types and nested
sub directories to confirm N levels of sub directory recursion.

Demo Project File Structure
- /HOME/find-python/testPyPath/*
- /HOME/find-python/testPyPath/myText.txt, myRoot.py
- /HOME/find-python/testPyPath/subPyRes/refPy.py, resPy.py
- /HOME/find-python/testPyPath/subPyPath/anoText.txt, mySubPath.py
- /HOME/find-python/testPyPath/subPyPath/subMergePath/README.md, submarine.py


### EXECUTE SCRIPT findPython.py ###

`findPython.py` can reside in the HOME directory or copied to the Python
versions installed parent. Depending on how Python was installed, the parent 
directory can include multiple installed Python versions or just one.
The benefit of this script is that it can recurse down through multiples levels
within the parent file structure.

NOTE: Locations may/will vary
<br/>Ex. Windows User Space Installed
<br/>-> C:\Users\USER\AppData\Python # parent can have multiple versions installed.
<br/>cmd: python ../../../findPython.py # same-as python C:\Users\USER\findPython.py
<br/>
<br/>Ex. MacOS Homebrew Installed
<br/>-> /opt/homebrew/Cellar # can have multiple version installed.
<br/>cmd: python ../../../findPython.py # same-as python /Users/USER/findPython.py 

STNDOUT:
- csv file: /Users/RACF/Documents/python.pyp.csv
- removing: ./myRoot.py
- removing: ./subPyRes/resPy.py
- removing: ./subPyRes/refPy.py
- removing: ./subPyPath/mySubPath.py
- removing: ./subPyPath/subMergePath/submarine.py
- done removing files! See removed in /Users/USER/Documents/python.pyp.csv

Expand any sub directory and only the non-python files remain.


### SCRIPT PROCESS ###

`findPython.py` defines three methods that complete:
1. Recursively search for .py files under the executed parent directory,
   including N level of sub directories under the parent..
2. Appends .py files relative path (to parent) to a List with found files.
3. List item path/file.py' are written to a .csv file, saved under the 
   /HOME/Documents directory with the name `python.pyp.csv`
4. Reads in the line separated .csv file of .py's to be removed. 
5. Iterates over each path/file.py until the end of the document
   and removes files that path.exists() is true.

NOTE 1: This process is atomic and should ONLY be run in the User space
  and under a known directory where Python user installed versions exist.
  <br/>-> Windows User installed (typically) be: `C:\Users\USER\AppData\Python`
  <br/>-> Mac Homebrew installed will be:  `/opt/homebrew/Cellar/`

NOTE 2: findPython.py can reside in the users HOME directory and will work 
     from HOME directory, but that risks removing System required python files 
     that should be included for critical system or application operation.<br/>
     For example, on MacOS, application support resources are located under 
     HOME/Library/Application Support/* which my break application functionality
     if Python is a dependency.
