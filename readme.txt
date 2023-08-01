Have to set up a virtual environment to run on a local host.
IDE used: visual studio code

setting up venv:
1. in powershell run 'python -m venv .venv'

1.5 if you do not have the PowerShell extension for VSC install it from the extensions tab then do step 1

2. run '.venv\Scripts\Activate.ps1' in the same directory at the manage.py file

2.5 if you get a script running denial/error run this line: 'Set-ExecutionPolicy -Scope CurrentUser Unrestricted' then try step 2 again

3. when in venv, pip install python, black, and django
    3.1 python -m pip install black
    3.2 python -m pip install django
    3.2 python -m pip install pillow

4. run the line 'python manage.py runserver' to run app. Default address and port is http://127.0.0.1:8000/
