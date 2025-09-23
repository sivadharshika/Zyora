from mongoengine import Document, StringField, DateTimeField, IntField, ListField, EmailField
from uuid import uuid4
from datetime import datetime

class User(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    name = StringField(required = True)
    email = EmailField(required = True, unique = True)
    phone = StringField(unique = True)
    password = StringField(required = True)
    gender = StringField(required = True, choices = ["male", "female"])

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()