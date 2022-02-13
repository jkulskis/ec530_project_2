import json
from patient_monitor import patient

def add_device_data(
    patient_id: int,
    temp: float = None,
    blood_pressure: float = None,
    pulse: float = None,
    oxygen_level: float = None,
    weight: float = None,
    glucose_level: float = None,
) -> None:
    patient.modify_patient(
        patient_id=patient_id,
        temp=temp,
        blood_pressure=blood_pressure,
        pulse=pulse,
        oxygen_level=oxygen_level,
        weight=weight,
        glucose_level=glucose_level,
    )