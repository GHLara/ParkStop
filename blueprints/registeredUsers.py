import models.Users
from flask import request
from flask import Blueprint, render_template, redirect, url_for

registeredUsers = Blueprint("registeredUsers", __name__, template_folder="./templates/", static_folder='./static/', root_path="./")


@registeredUsers.route("/registeredUsers")
def registeredUsersIndex():
    userlist = []
    for user in models.Users.users:
      nome = user.nome
      email = user.email
      userlist.append([nome, email])
    
    return render_template("/managment/registeredUsers.html", users = userlist)
