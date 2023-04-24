import os
import subprocess
import zipfile

class GestionFichers :

    def _init_(self) -> None:
        self.RechercherFichier = []
        
    def Chemin(self,path):
        Liste = []
        for l in os.listdir(path) :
            if l[0] != '.':
                Liste.append({
                    'chemin':path+"/"+l,
                    'nom' : l
                })
        return Liste
    
    def DirectoryUser(self, path : str) :
        Liste : list[str] = []
        try: 
            for i in os.listdir(path) : 
                if os.path.isdir(path+"/"+i) :
                    Liste.append(i)
        except :
            return []
        return Liste

    def FileUser(self, path : str) :
        Liste : list[str] = []
        try :
            for i in os.listdir(path) : 
                if os.path.isfile(path+"/"+i) :
                    Liste.append(i)
        except :
            return []
        return Liste
          
    def NbrFiles(self, path : str) -> int :
        compteur : int = 0
        try:
            for l in os.listdir(path) : 
                if os.path.isfile(path+"/"+l) and l[0] != '.':
                    compteur += 1
        except :
            return 0
        return compteur

    def NbrDir(self, path : str) -> int : 
        compteur : int = 0
        try :
            for l in os.listdir(path) : 
                if os.path.isdir(path+"/"+l) :
                    compteur += 1
        except:
            return 0
        return compteur
          
    def TailleF(self, path : str) -> None :
        Commande = ['du', '-s', path]
        try:
            return subprocess.run(Commande, capture_output=True, text=True).stdout.split()[0]
        except:
            return 0
        
    
    def FichierEXT(self,path:str,NomFichier : str )  : 
        liste = []
        try:
            for i in os.listdir(path) :
                if i[0] != '.':
                    if(i.count(NomFichier)): 
                        liste.append({
                            'chemin':path+"/"+i,
                            'nom' : i
                        })
        except:
            return []
        return liste
    
    def Telecharger(self,username) -> None :
        home_dir = os.path.expanduser('/home/'+username)
        zip_filename = "/home/"+username+"/"+username+".zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(home_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, home_dir))
          
      
if _name_ == "_main_" :
    f= Filesanddirs()
    f.getPath("/home/a")