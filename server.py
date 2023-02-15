from flask import Flask
from flask import render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(url="https://api.agify.io", params={"name": name})
    age = age_response.json()["age"]
    gender_response = requests.get(url="https://api.genderize.io", params={"name": name})
    gender = gender_response.json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = blog_response.json()
    return render_template("blog.html", post=all_post)



if __name__ == "__main__":
    app.run(debug=True)