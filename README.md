# Project 2: Patient Monitor
## John Mikulskis
### EC530 Project 2

## Installation
Install required dependencies with pip:
```
pip install -r requirements.txt
```

## Usage

### Patient Management
Patients can be added or removed from the system using `add_patient(patient_id: int)` and `remove_patient(patient_id: int)` respectively. The `patient_id` passed to `add_patient()` must not already exist, and the `patient_id` passed to `remove_patient()` must already exist.

### Devices
Devices can create or modify data for patients with the device module. Use add_device_data to create or modify existing patient data. The only required parameter is the patient id, an integer used to identify the patient. Other parameters are passed as necessary based on the device that is sending over the data.

```python3
add_device_data(
    patient_id: int,
    temp: float = None,
    blood_pressure: float = None,
    pulse: float = None,
    oxygen_level: float = None,
    weight: float = None,
    glucose_level: float = None,
)
```

e.g. An oximeter would call `add_device_data()` with the `patient_id` parameter and the `oxygen_level` parameter. If the patient id exists, then their data is updated to reflect this new device measurement.

## Tests
Run tests by executing `pytest` in the root directory

## Workflow (Branches)
A branch is created off of main to add a new feature, bug-fix, or other change. Once the work is finished and actions on this branch run succesfully, then the work should be squashed and merged into the main branch.

## Note
Currently, the data is dumped into a json file located at `data/patient_data.json`, but we will update this to a database in the near future with one of our feature tickets