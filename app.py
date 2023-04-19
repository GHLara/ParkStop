from flask import Flask, render_template

from blueprints.auth import auth
from blueprints.registeredUsers import registeredUsers
from blueprints.sensorData import sensorData

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(registeredUsers, url_prefix='/registeredUsers')
app.register_blueprint(sensorData, url_prefix='/sensorData')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)