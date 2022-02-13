import json

# TODO: Use a real db instead of json file
DATA_FILE = 'data/patient_data.json'
try:
    patient_db = json.loads(DATA_FILE)
except:
    patient_db = {}

def update_patient_db():
    with open(DATA_FILE, 'w') as write_file:
        json.dump(patient_db, write_file)

def add_patient(patient_id: int):
    """Add a patient to the db

    Args:
        patient_id (int): unique id for the patient
    """
    if patient_id in patient_db:
        raise ValueError(f"Patient {patient_id} Already Exists")
    patient_db[patient_id] = {
        "temp": None,
        "blood_pressure": None,
        "pulse": None,
        "oxygen_level": None,
        "weight": None,
        "glucose_level": None,
    }
    update_patient_db()

def remove_patient(patient_id: int):
    """Remove a patient from the db

    Args:
        patient_id (int): unique id of the patient
    """
    if patient_id not in patient_db:
        raise KeyError(f"Patient {patient_id} Does Not Exist")
    patient_db.pop(patient_id)
    update_patient_db()

def modify_patient(patient_id: int, **kwargs):
    """Modify different attributes (kwargs) of a patient's data. If kwargs
    have a value of None then they will be skipped

    Args:
        patient_id (int): unique id of the patient
    """
    if patient_id not in patient_db:
        raise KeyError(f"Patient {patient_id} Does Not Exist")
    unmodified_patient_data = patient_db[patient_id].copy()
    for k, v in kwargs.items():
        if v is None:
            continue
        if k not in patient_db[patient_id]:
            # must modify all kwargs or none of them
            patient_db[patient_id] = unmodified_patient_data
            raise ValueError(f"Invalid Patient Data Key: {k}")
        patient_db[patient_id][k] = v
    update_patient_db()

def reset_patient(patient_id: int):
    """Set all attributes of a patient's data to None

    Args:
        patient_id (int): unique id of the patient
    """
    if patient_id not in patient_db:
        raise KeyError(f"Patient {patient_id} Does Not Exist")
    for k in patient_db[patient_id].keys():
        patient_db[patient_id][k] = None
    update_patient_db()