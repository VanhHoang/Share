## Share

# Config
* git config --global user.name "User Name"
* git config --global user.email "username@gmail.com"

# Clone Git
* git clone https://github.com/VanhHoang/Share.git
* git clone --single-branch --branch manager_user_p2 https://github.com/Dungprj/shoppe_nhom_06.git

# Create 
* git init

# Branch

* git branch <name_branch>
* git checkout <name_branch>
* =>
* git checkout -b <name_branch>

* git push -u <remote> <name_branch>

# PUSH
* git add <name_file>     <->       git add .
* git commit -m "name_commit"
* git push -u origin master 

# Remote
* git remote add origin https://github.com/VanhHoang/Share.git

# Pull
* git pull origin master

## ENV PYTHON 

# Download package
* pip install virtualenv

# Create env
* Windows: py -m venv myworld
* Unix/MacOS: python -m venv myworld
or
# Select env
* Windows: py ...
* Unix/MacOS: python -m virtualenv -p 'C:\Users\username\AppData\Local\Programs\Python\Python311\python.exe' env

# CMD 
* cd 
* dir/ls

  
# Activate
* Windows: myworld\Scripts\activate.bat
* Unix/MacOS: source myworld/bin/activate

# NOTE: With PowerShell, if you can't use "activate"
*  First Solution: Set-ExecutionPolicy Unrestricted -Scope Process
*  Second Solution: Set-ExecutionPolicy Unrestricted -Force


