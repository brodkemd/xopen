import os, sys

code_dir = False
code_counter = 0

# default file opener
def default(file): os.system("xdg-open \"" + file +"\"")

# opens the inputted file in vscode
def code(file):
    os.system("code \"" + file + "\"")

    # counts the file that was opened    
    global code_counter
    code_counter+=1


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


# opens the current directory
def dir(path):
    # goes through the files at the inputted path and sees if a file type has a special extension to be handled accordingly
    for item in os.listdir(path):
        file_opener(os.path.join(path, item), enable_default_handler=False)

    # opens the inputted path in vscode if there is a file in the directory that requires it or if there were more than 3 files
    if code_dir or code_counter >= 3: code(path)


'''

Begin file type functions

'''

def latex(file):
    # splits the inputted file path in the file name and its directory
    tail, head = os.path.split(file)
    
    # reads the data from the latex file
    with open(file, 'r') as f: data = f.read()

    # if there is no data in the file, then data is added to make it a working latex file
    if not len(data):
        # writes the data required for it to be a working latex file to it
        with open(file, 'w') as f:
            f.write("\\documentclass[12pt]{article}\n\\begin{document}\nHello\n\\end{document}")

        # if there is not a pdf file for the latex file already, it is generated
        if file.replace(".tex", ".pdf") not in os.listdir(tail):
            # making the file
            os.system("pdflatex -interaction=nonstopmode " + file)
            os.system("xdg-open \"" + file.replace(".tex", ".pdf") +"\"")
    
    global code_dir
    code_dir = True

'''

The code really begins here

'''

# commands correspinding to a certain file extension
extension_commands = {".tex" : latex,
                      ".txt" : code,
                      ".pdf" : default}

for i in range(1, len(sys.argv)):
    # checks if the item in the inputted args is a directory, opens it with the dir method
    if os.path.isdir(sys.argv[i]): dir(sys.argv[i])

    # the path is a file, opening it accordingly
    else: file_opener(sys.argv[i])