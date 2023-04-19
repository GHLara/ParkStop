from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint("auth", __name__, template_folder="./views", static_folder='./static/', root_path="./")

registered = ["Admin", "123"]

atual_user = ""

@auth.route("/login")
def authLogin():
    return render_template("auth/login.html")

@auth.route("/register")
def authRegister():
    return render_template("auth/register.html")

@auth.route("/loggedPage")
def authLogged():
    return render_template("/auth/authLogged.html", user = atual_user)

@auth.route("/loggedAdminPage")
def authAdminLogged():
    return render_template("/auth/authAdminLogged.html", user = atual_user)

@auth.route("/authentication", methods = ['POST', 'GET'])
def authentication():
    global registered
    global atual_user
    if request.method == 'POST':
        usuario = request.form['user']
        senha = request.form['password']
        if (usuario == "Admin") and (senha == "123"):
            atual_user = usuario
            return redirect(url_for("auth.authAdminLogged"))
        if (usuario in registered) and (senha in registered) and (usuario != senha) :
            atual_user = usuario
            return redirect(url_for("auth.authLogged"))
        else:
            return redirect(url_for("auth.auth_login_faield"))
