from flask import Flask, render_template, request, session, redirect
from models.character import Charater
from models.user import User
import mlab

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "very secret"

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
     if "token" in session:
      character_list = Charater.objects()
      return render_template("characters.html",c_list = character_list)
     else:
          return redirect("/login?next=/characters")


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

@app.route("/login", methods=["GET","POST"])
def login():
     if request.method == "GET":
          return render_template("login_form.html")
     elif request.method == "POST":
          form = request.form
          username = form["username"]
          password = form["password"]
          found_user = User.objects(username=username).first()
          if found_user is None:
               return "User Not found"
          elif found_user.password != password:
               return "Invalid password"
          else:
               session["token"] = username
               next = request.args.get("next")
               if next is None or next == "":
                 return "Logged in succesfully"
               else:
                    return redirect(next)


     @app.route("/logout")
     def logout():
          del session["token"]
          return redirect("/login")
          if username == "admin" and password == "admin":
            session["token"] = "admin"
            return "Logged in succesfully"
          else:
            return "Failed to login"
     return render_template("login_form.html")


@app.route('/posts')
def posts():
     if "token" not in session:
          return redirect("/login?next=/posts")
     else:
          username = session["token"]





if __name__ == "__main__":
  app.run( debug=True)
 