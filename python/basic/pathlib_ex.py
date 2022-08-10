import pathlib

pathlib.Path.home() 
pathlib.Path.cwd()

XX = pathlib.Path("PATH NAME")

# get the folder path of the current file
pathlib.Path(__file__).parent
