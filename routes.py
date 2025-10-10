import os
import smtplib
from flask import Blueprint, render_template, request, flash, redirect, url_for, session

main = Blueprint('main', __name__)

EMAIL_KEY = ""
PASSWORD_KEY = ""

@main.route('/set_language/<lang_code>')
def set_language(lang_code):
    session['lang'] = lang_code
    return redirect(request.referrer or url_for('main.index'))

@main.route('/')
def index():
    return render_template("index.html")


@main.route('/moviereviewers')
def movie_reviewers():
    return render_template("moviereviewers.html")

@main.route('/myfilmsay')
def myfilmsay():
    return render_template("myfilmsay.html")


@main.route('/steamchests')
def steam_chests():
    return render_template("steamchests.html")


@main.route('/otherprojects')
def other_projects():
    return render_template("otherprojects.html")


@main.route('/datascience')
def data_science():
    return render_template("datascience.html")


MAIL_ADDRESS = os.environ.get("EMAIL_KEY")
MAIL_main_PW = os.environ.get("PASSWORD_KEY")

@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL_ADDRESS, MAIL_main_PW)
        connection.sendmail(MAIL_ADDRESS, MAIL_main_PW, email_message)