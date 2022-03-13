from typing import List, Union
from db import db
import time
import patient
import datetime


class Chat:
    def __init__(self, sender: int, to: Union[List[int], int], content: str):
        self.sender = sender
        self.to = [to] if isinstance(to, int) else sorted(to)
        self.content = content

    def is_valid(self):
        # message must be less than or equal to 1000 chars
        if len(self.content) > 1000:
            return False
        # need at least 2 chatters
        if len(set(self.members)) < 2:
            return False
        # Check if all members exist in the patients db
        for patient_id in self.members:
            try:
                patient.get_patient(patient_id)
            except:
                return False
        return True

    @property
    def members(self):
        return sorted(self.to + [self.sender])

    @property
    def document(self):
        return {
            "sender": self.sender,
            "to": self.to,
            "content": self.content,
            "timestamp": time.time(),
            "timestamp_readable": datetime.datetime.now(),
        }


def get_chat_history(members: List[int]):
    """Get chat history for these member ids if it exists"""
    chat_history = db.chats.find_one({"members": sorted(members)})
    # Don't raise if chat_history is None, instead just return the None value
    return chat_history


def remove_chat_history(members: List[int]) -> bool:
    """Remove chat for these member ids if it exists"""
    del_result = db.chats.delete_one({"members": sorted(members)})
    return del_result.deleted_count == 1


def send_chat(chat: Chat):
    """Get chat history for these member ids if it exists"""
    if not chat.is_valid():
        raise ValueError("Chat is not valid. Check length or member ids")
    # use $all since order of members does not matter
    if db.chats.find_one({"members": chat.members}) is None:
        db.chats.insert_one(
            {
                "members": chat.members,
                "messages": [],
                "timestamp": time.time(),
            }
        )
    updates = {
        "$push": {
            "messages": chat.document,
        }
    }
    update_result = db.chats.update_one({"members": chat.members}, updates)

    if not update_result.matched_count:
        raise ValueError(f"Error sending chat message. Did not update chat history")
