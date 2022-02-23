from patient_monitor import device, patient
import random

def test_add_new_patient():
    patient_id = random.randint(0, 1e7)
    patient.add_patient(patient_id)
    assert patient.get_patient(patient_id)['weight'] is None
    device.add_device_data(patient_id, weight=200)
    assert patient.get_patient(patient_id)['weight'] == 200
    patient.remove_patient(patient_id)