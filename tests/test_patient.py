from patient_monitor import patient
import random

def test_add_new_patient():
    patient_id = random.randint(0, 1e7)
    assert patient_id not in patient.patient_db
    patient.add_patient(patient_id)
    assert patient_id in patient.patient_db
    patient.remove_patient(patient_id)

def test_remove_patient():
    patient_id = random.randint(0, 1e7)
    patient.add_patient(patient_id)
    assert patient_id in patient.patient_db
    patient.remove_patient(patient_id)
    assert patient_id not in patient.patient_db
    
def test_modify_patient():
    patient_id = random.randint(0, 1e7)
    patient.add_patient(patient_id)
    assert patient.patient_db[patient_id]['weight'] is None
    patient.modify_patient(patient_id, weight=200)
    assert patient.patient_db[patient_id]['weight'] == 200
    patient.remove_patient(patient_id)

