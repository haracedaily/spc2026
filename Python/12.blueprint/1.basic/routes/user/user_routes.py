from flask import Blueprint, render_template

user_blueprint = Blueprint("user",__name__, template_folder="../../templates/user")

@user_blueprint.route('/')
def user_page():
    return render_template("user.html")

@user_blueprint.route('/<id>')
def search_user(id):
    return render_template("user/user.html",id)