# Python GUI mouse and keyboard control
personal testing room for python gui library
- - - -
## Installation
1. install Python
2. create virtual environment `virtualenv -p="<your_python.exe_version_path_here>" venv` (or `pip install virtualenv` globally if you dont have one yet)
3. install packages inside venv via `source venv/Scripts/activate`. your cli should have `(venv)` on the top
4. check if it is installed correctly via `which python` / `which pip` and a list of installed packages in venv via `pip list`
5. run python files within **this** virtual environment
6. to step away from this venv, type `deactivate` in cli

## Reminder
- your python 3.7 executable path is `"C:\Users\skbra\AppData\Local\Programs\Python\Python37\python.exe"`
- this repo use python 3.7.0, package : pywin32 (pythoncom), pyHook [install via .whl [pythonlibs](https://www.lfd.uci.edu/~gohlke/pythonlibs/)], pythonautogui