import os
import spwd
import crypt 

class Login :
    def _init_(self,Nom_utilisateur : str,MotdePasse : str) :
        self.Nom_utilisateur = Nom_utilisateur
        self.MotdePasse = MotdePasse

    def TestNomUtilisateur(self) -> bool :
        if self.Nom_utilisateur in os.listdir("/home") :
            return True
        else :
           
            return False
    def TestMotdepasse(self,Nom_utilisateu:str,MotdePasse:str) -> bool :
        user=spwd.getspnam(Nom_utilisateu)
        if(crypt.crypt(MotdePasse, user.sp_pwdp)) == user.sp_pwdp:
            return True
        return False
           
        return False
    def TestFinal(self)->bool :
        if (self.TestNomUtilisateur == True and self.TestMotdepasse ==True ) :
            return True
        else :
            print("Error !!!!")
            return False

if _name_ == "_main_" :
     a = Login("alich","1234")
    
    
