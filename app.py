from flask import Flask, render_template, request
from models.character import Charater
import mlab
mlab.connect()
app = Flask(__name__)

# Character.objects() lay het du lieu ra

@app.route("/add_character", methods = ["GET","POST"]) # vs phuong thuc POST phai chinh o ca html va sever
def add_character():
    #1 gui form (GET)
    if request.method == "GET":
     return render_template("character_form.html")
    elif request.method == "POST":
    #4 nhan form => luu (POST)
     form = request.form
     name = form["name"]
     image = form["image"]
     rate = form["rate"]
     new_character = Charater(name =name,image=image,rate=rate)
     new_character.save()
    
     return "Gotcha"
@app.route("/characters")
def character():
    character_list = Charater.objects()
    return render_template("characters.html",c_list = character_list)
@app.route("/character/<given_id>")
def character_detail(given_id):
    # #1. Get one character, dua vao id   
    # character = charater.objects(id=given_id).first()
    # print(character)
    character = Charater.objects().with_id(given_id)

    if character is None:
     return "Not Found"
    else:
     return render_template("character_detail.html",character = character)

if __name__ == "__main__":
  app.run( debug=True)
 