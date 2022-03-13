from patient_monitor import patient
import chat
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

def test_new_chat():
    members = []
    for i in range(2):
        members.append(add_random_new_patient())
    new_chat = chat.Chat(
        sender=members[0],
        to=members[1],
        content="Test Chat"
    )
    chat.send_chat(new_chat)
    chat_history = chat.get_chat_history(members)
    assert chat_history is not None
    assert chat_history["messages"][0]["content"] == "Test Chat"
    assert chat_history["messages"][0]["sender"] == members[0]
    chat.remove_chat_history(members)

def test_new_group_chat():
    members = []
    for i in range(3):
        members.append(add_random_new_patient())
    new_chat = chat.Chat(
        sender=members[0],
        to=members[1:],
        content="Test Group Chat"
    )
    chat.send_chat(new_chat)
    chat_history = chat.get_chat_history(members)
    assert chat_history is not None
    assert chat_history["messages"][0]["content"] == "Test Group Chat"
    assert chat_history["messages"][0]["sender"] == members[0]
    chat.remove_chat_history(members)

