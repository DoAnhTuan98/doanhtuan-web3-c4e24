from flask import Flask, render_template, request
app = Flask(__name__)
import mlab
from models.bike import Bike
mlab.connect()
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/new_bike", methods=["POST","GET"])
def newbike():
    if request.method == "GET":
        return render_template("add_bike.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        daily = form["daily"]
        image = form["image"]
        year = form["year"]
        new_bike = Bike(model=model,daily=daily,image=image,year=year)
        
        new_bike.save()
        return("hello")
        

if __name__ == "__main__":
  app.run( debug=True)
 