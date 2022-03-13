# Project 2: Patient Monitor
## John Mikulskis
### EC530 Project 2

## Installation
Install required dependencies with pip:
```
pip install -r requirements.txt
```

## Flask Endpoints
| Page Name | Endpoint | Method | Notes | 
| -------- | ------- | ------ | ---- |
| Welcome page (index) | / | [GET] | |
| Help | /help | [GET] | |
| Get patient info | /patient/{int:patient_id} | [GET] | |
| Create a patient | /patient/create/{int:patient_id} | [POST] | |
| Add device data | /device/add-data/{int:patient_id} | [POST] | Send new key/values as query params
| Send a chat | /chat/{int:patient_id} | [POST] | `to` and `content` query params. `to` can be multiple ids for group chats |
| Get chat history | /chat | [GET] | `members` query param |
| Remove chat history | /chat/remove | [POST] | `members` query param |

## Functional Usage

### Patient Management
Patients can be added or removed from the system using `add_patient(patient_id: int)` and `remove_patient(patient_id: int)` respectively. The `patient_id` passed to `add_patient()` must not already exist, and the `patient_id` passed to `remove_patient()` must already exist.

### Patient Storage
Currently, the data is dumped into a mongodb db located in the cloud (URI stored in secrets)

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

### Chat
There is a chat funcitonality for patients to open up a new chat with a doctor or other physician. To start a chat, simply post to the endpoint `/chat/{int:patient_id}` where `patient_id` is the patient or doctor sending the chat, and they can send the chat to 1 of more patients/doctors by specifying their ids with the query param `to` and the chat with the query param `content`

e.g. Send a chat saying "Hello World" from patient 0 to patients 1 and 2: `POST /chat/0?to=1,2&content=Hello World`

This chat will be stored in the MongoDB

To access chat history, send a get request to `/chat` with a query param `members` representing everyone involved in the chat.

e.g. To access the above chat records between ids 0, 1, and 2: `GET /chat?members=0,1,2`

Note: All member ids involved must exist to post a chat, and the chat message must be <= 1000 chars

## Tests
Run tests by executing `pytest` in the root directory. Tests also connect to the cloud db, so `MONGO_URI` must be set as an env variable or in a config toml file in the `patient_monitor` dir.

## Workflow (Branches)
A branch is created off of main to add a new feature, bug-fix, or other change. Once the work is finished and actions on this branch run succesfully, then the work should be squashed and merged into the main branch.

## Cloud
Currently hosting this version on AWS Elastic Beanstalk: 
http://patientmonitorec530-env.eba-dnv2imbb.us-east-2.elasticbeanstalk.com/

## Note
We will soon move the application to the cloud, instead of just the db
