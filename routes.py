from flask import Blueprint, render_template, request, flash, redirect, url_for, session

main = Blueprint('main', __name__)


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