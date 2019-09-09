# Generals
import uuid
import os

# Specifics
from Utilities.DateHandler import today_YYYYMMDD, hour_HHMMSS
from Logs.Constants import log_folder
from Utilities.GeneralConstants import absolute_path_project_folder

# Tools to create a TXT Report
#   Handler().__init__(...) receives pRelativePath which indicates the
#   folder in Logs --> .../.../Logs/[pRelativePath]/[file_name].txt
#
# For develeloping purpose, the reports are created in the 'Logs/[specific_report_folder]'
# project folder
# Actually, they should be written in an extenernal server folder.


class Handler():
    # If class and/or method are empty, pass as '' (empty string)
    def __init__(self, pRelativePath, pFile, pClass, pMethod, pException):
        self.relativePath = pRelativePath # path where the file will be save
        self.fileName = pFile
        self.className = pClass
        self.methodName = pMethod
        self.exception = pException # original exception --> takes its attributes to generate the report's content
        self.uniqueID = str(uuid.uuid4()) # used to generate a unique name to not replace existing files

        # Create .txt report
        self.LogGenerator()

    def LogGenerator(self):
        path = absolute_path_project_folder + "/" + log_folder + "/" + self.relativePath # [...]\ServigariAPI_Python\Logs\[input path]
        name = self.fileName + "_"

        #It's possible the exception doesn't come from a Class
        name += 'NoClass_' if self.className == '' else self.className + '_'

        #It's possible the exception doesn't come from a method
        name += 'NoMethod_' if self.methodName == ''  else self.methodName + '_'

        name += today_YYYYMMDD + "_" + hour_HHMMSS + "_" + self.uniqueID + ".txt"
        final_path = os.path.join(path  + "/", name) # Define absolute path
        
        e = Exception(self.exception)
        description = 'Exception: ' + str(e) + "\n"
        description += 'Cause: ' + str(e.__cause__) + "\n"

        self.CreateTXT(final_path, description)

    def CreateTXT(self, pPath, pDescription):
        f = open(pPath, "w+") # Open with write permits - f is the file object
        f.write('File: ' + self.fileName + "\n")
        f.write('Class: ' + self.className + "\n")
        f.write('Method: ' + self.methodName + "\n")
        f.write(pDescription) # Write the content
        f.close()