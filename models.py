from mongoengine import Document, StringField, DateTimeField, IntField, ListField, EmailField, BooleanField
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


class NailArt(Document):
    
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    category = StringField(required = True)
    title= StringField(requried =True)
    describtion = StringField()
    issaved= BooleanField()
    sharelink= StringField()
    availableOn =ListField(require= True)
    image = StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class Category(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    category = ListField(choices=["normalArt", "designArt", "gilterArt", "colourfullArt"])
    title = StringField(requried =True)
    description = StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class Dress(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    image=StringField(required = True)
    title=StringField(required = True)
    description=StringField(required = True)
    category=StringField(required = True)
    availableOn=ListField(required =  True)
    isSaved=BooleanField()
    shareLink=StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()


class Ornaments(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    image =  StringField(required = True)
    title = StringField(required = True)
    description = StringField(required = True)
    category = StringField(required = True)
    sharelink = StringField()
    availableon = ListField(required = True)
    isSaved = BooleanField()
    
    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()



    