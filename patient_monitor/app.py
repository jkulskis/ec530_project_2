import toml
import os
from flask import Flask, abort, jsonify, request


def create_app():

    app = Flask(__name__)
    #### MONGO URI
    try:
        app.config.from_file("config.toml", load=toml.load)
    except:
        pass
    try:
        app.config["MONGO_URI"] = os.environ["MONGO_URI"]
    except KeyError:
        pass
    ######
    return app

app = application = create_app()
with app.app_context():
    import db
import patient, device

if __name__ == "__main__":
    app.run()

@app.route("/", methods=["GET"])
def home():
    return "Welcome to patient monitor. Visit /help for more information"


@app.route("/help", methods=["GET"])
def help_default():
    return """
        Welcome page (index):\t/\t[GET]<br>
        Help (this page):\t/help\t[GET]<br>
        Get patient info:\t/patient/{int:patient_id}\t[GET]<br>
        Create a patient:\t/patient/create/{int:patient_id}\t[POST]<br>
        Add device data:\t/device/add-data/{int:patient_id}\t[POST]<br>
    """


@app.route("/patient/<int:patient_id>", methods=["GET"])
def patient_info(patient_id: int):
    try:
        return jsonify(patient.get_patient(patient_id))
    except ValueError as e:
        abort(404, description=e)


@app.route("/patient/create/<int:patient_id>", methods=["POST"])
def create_patient(patient_id: int):
    try:
        patient.add_patient(patient_id)
        return jsonify(patient.get_patient(patient_id))
    except ValueError as e:
        abort(400, description=e)


@app.route("/device/add-data/<int:patient_id>", methods=["POST"])
def add_device_data(patient_id: int):
    try:
        device.add_device_data(patient_id, **request.args)
        return jsonify(patient.get_patient(patient_id))
    except ValueError as e:
        abort(404, description=e)
