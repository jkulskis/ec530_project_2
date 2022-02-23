from patient_monitor import patient
import random

def add_random_new_patient():
    while 1: # get a patient id we haven't used yet
        patient_id = random.randint(0, 1e7)
        try:
            patient.get_patient(patient_id)
        except:
            break
    patient.add_patient(patient_id)
    return patient_id

def test_add_new_patient():
    patient_id = add_random_new_patient()
    assert patient.get_patient(patient_id)
    patient.remove_patient(patient_id)

def test_remove_patient():
    patient_id = add_random_new_patient()
    assert patient.get_patient(patient_id)
    patient.remove_patient(patient_id)
    try:
        patient.get_patient(patient_id)
        assert 0, f"Patient {patient_id} was never removed"
    except:
        pass
    
def test_modify_patient():
    patient_id = add_random_new_patient()
    assert patient.get_patient(patient_id)['weight'] is None
    patient.modify_patient(patient_id, weight=200)
    assert patient.get_patient(patient_id)['weight'] == 200
    patient.remove_patient(patient_id)

