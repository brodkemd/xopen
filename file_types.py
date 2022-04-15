import os

def counter(func):
    global code_counter
    code_counter+=1

@counter
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