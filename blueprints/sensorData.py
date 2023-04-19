from models.parkingLots import parkingLots as pkl
from flask import request
from flask import Blueprint, render_template, redirect, url_for

sensorData = Blueprint("sensorData", __name__, template_folder="./templates/", static_folder='./static/', root_path="./")

@sensorData.route('/parkingLots')
def parkingLots():
    states = []
    for parking in pkl:
      state = parking.occupied
      states.append(state)
    return render_template("/managment/parkingLots.html", parkingStates = states)
