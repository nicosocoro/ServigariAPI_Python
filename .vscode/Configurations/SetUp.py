import os, sys

#Define all the initial configuration that must be done to run the application

def Initial():
    #Add  the current project directory to PYTHONPATH
    #to be able to import parent folder's files to any other child file
    sys.path.append(os.getcwd())