from flask import Flask , render_template ,request , send_file

from Authentification import SignIn
from GestionFichiers import Filesanddirs


import os

athf : SignIn
GF = Filesanddirs()

pathcurent : str = ""
fixUsername : str = ""

app = Flask(_name_,template_folder="index.html",static_folder = 'styles.css')


@app.route("/")
def homepage():
    return render_template("Login.html")

@app.route('/logout')
def logout():
    return render_template("Login.html")


@app.route("/authentification",methods =["GET","POST"])
def home():
    global fixUsername
    global pathcurent
    username : str = request.form['username']
    password : str = request.form['password']
    authi = SignIn(username,password)
    if username != "" :
        if authi.authentificationtest() == True:   
            Username = username
            pathcurent = "/home/"+username
            return render_template("home.html",directory = GF.getPath("/home/"+username) )
    return render_template("Login.html",erreur = "username or password incorrect ")





@app.route('/<path:path>/',methods =["GET"])
def routefolders(path):
    try :
        global pathcurent
        pathcurent = "/"+path
        if os.path.isdir(pathcurent):
            return render_template("home.html",directory = GF.getPath(pathcurent))
        elif os.path.isfile(pathcurent):
            f = open(pathcurent)
            return render_template("home.html",text = f.read())
    except :
        return "erreur"


@app.route('/retour',methods =["GET","POST"])
def back():
    global pathcurent
    t = pathcurent.split("/")
    if len(t) != 3 :
        pathcurent = ""
        for i in range(len(t)-1):
            pathcurent += t[i] + "/"
        pathcurent = pathcurent[:len(pathcurent)-1]
  
    if os.path.isdir(pathcurent):
       return render_template("home.html",directory = GF.getPath(pathcurent))


@app.route("/Telecharger")
def Telecharger():
    GF.Telecharger(fixUsername)
    return send_file("/home/"+fixUsername+"/"+fixUsername+".zip", as_attachment=True)


@app.route('/NbrFiles')
def nbrfiles():
    return render_template("home.html",directory = GF.getPath(pathcurent),fil = str(GF.NbrFiles(pathcurent)))


@app.route('/NbrDir')
def nbrdirs():
    return render_template("home.html",directory = GF.getPath(pathcurent),dir = str(GF.NbrD(pathcurent)))


@app.route('/space')
def space():
    return render_template("home.html",directory = GF.getPath(pathcurent),spa = str(GF.getSize(pathcurent)))

@app.route('/findfichier',methods =["GET","POST"])
def fileSearch():
    filename : str = request.form['file']
    return render_template("home.html",directory = GF.rechercheFilesNameFileExtention(pathcurent,filename))

if _name_ == '_main_':
    app.run()