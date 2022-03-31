from file_types import *
import os, sys

# general file opener
def file_opener(directory_item, enable_default_handler=True):
    for item in extension_commands:
        # if the file has the extension
        if item in directory_item: 
            #runs the command that corresponds to the file extension
            extension_commands[item](directory_item)

            #found a match, exits the loop
            break
    
    # if the default handler is enabled
    if enable_default_handler: default(directory_item)


# default file opener
def default(file): os.system("xdg-open \"" + file +"\"")

# opens the inputted file in vscode
def code(file): os.system("code \"" + file + "\"")


# commands correspinding to a certain file extension
extension_commands = {".tex" : latex,
                      ".txt" : code,
                      ".pdf" : default}


# opens the current directory
def dir(path):
    # opens the inputted path in vscode
    code(path)

    # goes through the files at the inputted path and sees if a file type has a special extension to be handled accordingly
    for item in os.listdir(path):
        file_opener(os.path.join(path, item), enable_default_handler=False)
        

'''
The code really begins here

'''
for i in range(1, len(sys.argv)):
    # checks if the item in the inputted args is a directory, opens it with the dir method
    if os.path.isdir(sys.argv[i]): dir(sys.argv[i])        

    # the path is a file, opening it accordingly
    else: file_opener(sys.argv[i])
