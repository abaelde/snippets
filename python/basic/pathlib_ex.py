import pathlib

pathlib.Path.home() 
pathlib.Path.cwd()

XX = pathlib.Path("PATH NAME")

# get the folder path of the current file
pathlib.Path(__file__).parent

# Add suffix
p = Path.home() / "image.png"               # "/Users/thibh/image.png"
p.parent / (p.stem + "-lowres" + p.suffix)  # "/Users/thibh/image-lowres.png"
