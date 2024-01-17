from flask import Flask, render_template
import requests

# The data is coming from JSON Bin through an API.
url_for_json = "https://api.npoint.io/65541dfad4a7044e001c"
response = requests.get(url_for_json)
json_data = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", json=json_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def posts(num):
    return render_template("post.html", num=num, json=json_data)

if __name__ == "__main__":
    app.run(debug=True)