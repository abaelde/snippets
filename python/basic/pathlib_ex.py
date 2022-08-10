import pathlib


pathlib.Path.home() 
pathlib.Path.cwd()


XX = pathlib.Path("PATH NAME")


dossier_utilisateur = Path.home()
dossier_courant = Path.cwd()


# Créer un chemin avec une liste de dossiers
home = Path.home()                        # PosixPath('/Users/thibh/')
dossiers = ['Projets', 'Django', 'blog']
home.joinpath(*dossiers)                  # PosixPath('/Users/thibh/Projets/Django/blog')


# Get the folder path of the current file
pathlib.Path(__file__).parent


# Récupérer les informations sur un chemin
p = Path("/Users/thibh/Documents/index.html")
p.name    # "index.html"
p.parent  # "/Users/thibh/Documents"
p.stem    # "index"
p.suffix  # ".html"
p.parts   # ("/", "Users", "thibh", "documents", "index.html")

p.exists()   # True
p.is_dir()   # False
p.is_file()  # True


# Add suffix
p = Path.home() / "image.png"               # "/Users/thibh/image.png"
p.parent / (p.stem + "-lowres" + p.suffix)  # "/Users/thibh/image-lowres.png"


# Création de Dossiers
dossier = Path("/Users/thibh/Documents/SiteWeb/sources/css") # Le dossier SiteWeb et ses sous-dossiers n'existent pas
dossier.mkdir(parents=True) # On peut tout créer d'un coup avec le paramètre parents

# Création / Suppression de fichiers
fichier = Path("/Users/thibh/Documents/SiteWeb/index.html")
fichier.touch()   # On crée le fichier
fichier.unlink()  # On supprime le fichier


# Scanner des dossiers
for f in Path.home().iterdir():
    print(f.name)
    
dossiers = [d for d in Path.home().iterdir() if d.is_dir()]

for f in Path.home().glob("*.png"): # avec filtre
  print(f.name)  
  
for f in Path.home().rglob("*.png"): # Récursif
  print(f.name)
    
    


