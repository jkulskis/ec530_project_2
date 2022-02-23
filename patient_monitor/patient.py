import json
from db import db

VALID_PATIENT_ATTRIBUTES = {
    "temp",
    "blood_pressure",
    "pulse",
    "oxygen_level",
    "weight",
    "glucose_level",
}


def get_patient(patient_id: int):
    """Get patient info"""
    patient = db.patients.find_one({"_id": patient_id})
    if patient is None:
        raise ValueError(f"Can't find pateint {patient_id}")
    return patient


def add_patient(patient_id: int):
    """Add a patient to the db

    Args:
        patient_id (int): unique id for the patient
    """
    if db.patients.count_documents({"_id": patient_id}, limit=1):
        raise ValueError(f"Patient {patient_id} Already Exists")
    new_patient = {
        "_id": patient_id,
        "temp": None,
        "blood_pressure": None,
        "pulse": None,
        "oxygen_level": None,
        "weight": None,
        "glucose_level": None,
    }
    db.patients.insert_one(new_patient)


def remove_patient(patient_id: int):
    """Remove a patient from the db

    Args:
        patient_id (int): unique id of the patient
    """
    del_result = db.patients.delete_one({"_id": patient_id})
    if not del_result.deleted_count:
        raise ValueError(f"Patient {patient_id} Does Not Exist")


def modify_patient(patient_id: int, **kwargs):
    """Modify different attributes (kwargs) of a patient's data. If kwargs
    have a value of None then they will be skipped

    Args:
        patient_id (int): unique id of the patient
    """
    updates = {"$set": {}}
    for k, v in kwargs.items():
        if v is None:
            continue
        if k not in VALID_PATIENT_ATTRIBUTES:
            raise ValueError(f"Invalid Patient Data Key: {k}")
        updates["$set"][k] = v
    update_result = db.patients.update_one({"_id": patient_id}, updates)
    if not update_result.matched_count:
        raise ValueError(f"Patient {patient_id} Does Not Exist")


def reset_patient(patient_id: int):
    """Set all attributes of a patient's data to None

    Args:
        patient_id (int): unique id of the patient
    """
    updates = {"$set": {}}
    for k in VALID_PATIENT_ATTRIBUTES:
        updates["$set"][k] = None
    update_result = db.patients.update_one({"_id": patient_id}, updates)
    if not update_result.matched_count:
        raise ValueError(f"Patient {patient_id} Does Not Exist")
