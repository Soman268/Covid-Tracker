from flask import Flask , render_template,redirect,url_for
import requests


app=Flask(__name__)

@app.route('/')

@app.route('/Information')
def Information():
   return render_template("information.html")    
 

@app.route("/home")
def home():
    return redirect(url_for('covid'))


@app.route("/covid")
def covid():
    
      
    data = requests.get("https://disease.sh/v2/countries/India?yesterday=true&strict=true")
    data_dict = data.json()
    return render_template("home.html",data=data_dict)

@app.route('/world')
def world():

    world = requests.get("https://corona.lmao.ninja/v2/all") 
    world_data = world.json()
    return render_template("world.html",world=world_data)  


@app.route('/contribute')
def contribute():
    return render_template("contribute.html") 


if __name__=="__main__":
    app.run()