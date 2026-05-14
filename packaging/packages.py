#Packages are used to store related modules
""" In order to use a folder as a package or subpackage, there has to
be an __init__.py file inside that folder.  """

from Modules.functions import *

sumar(1,2)

#Distributed package: if you install a distributed package 
# call packages from anywhere

#1. Create setup.py
#2. from the folder where is placed setup.py execute in terminal: python setup.py sdist
#3. Distribute .tar.gz file
#4. Install package: pip3 install .\modulefilename.tar.gz
#5. Uninstall packave pip3 uninstall packagename
