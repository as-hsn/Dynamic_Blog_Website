from flask import Flask, render_template, request
import requests
from smtplib import SMTP

## SMTP module for sending all details of the contact page form via email.

# FROM_ADDR = ""
# TO_ADDR = ""
# PASSWORD = ""
# mail = SMTP("smtp.gmail.com")
# mail.starttls()
# mail.login(user="", password=PASSWORD)


# The data is coming from JSON Bin through an API.
url_for_json = "https://api.npoint.io/65541dfad4a7044e001c"
response = requests.get(url_for_json)
json_data = response.json()


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", json=json_data)


@app.route ("/about")
def about() :
    return render_template ("about.html")


@app.route("/post/<int:num>")
def posts(num):
    return render_template("post.html", num=num, json=json_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["username"]
        email = data["email"]
        phone_number = data["phonenumber"]
        message = data["message"]
        # mail.sendmail(from_addr=FROM_ADDR, to_addrs=TO_ADDR, msg=f"Subject:BLOG WEBSITE\n\nName:{name}\nEmail:{email}\nPhone:{phone_number}\nMessage:{message} ")
        # mail.close()
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
