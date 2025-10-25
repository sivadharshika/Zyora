from mongoengine import Document, StringField, DateTimeField, IntField, ListField, EmailField, BooleanField, ReferenceField, CASCADE
from uuid import uuid4
from datetime import datetime

class User(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    name = StringField(required = True)
    email = EmailField(required = True, unique = True)
    phone = StringField(unique = True)
    password = StringField(required = True)
    gender = StringField(choices = ["male", "female"])

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class Category(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    category = StringField(choices=["dress", "nailArt", "ornaments", "hairStyle"])
    title = StringField(requried =True)
    description = StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class Dress(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    image=StringField(required = True)
    title=StringField(required = True)
    description=StringField(required = True)
    category=ReferenceField(Category, required = True, null=True)
    availableOn=ListField()
    isSaved=BooleanField()
    shareLink=StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()


class SaveDress(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    dress=ReferenceField(Dress, required = True, reverse_delete_rule=CASCADE)
    user=ReferenceField(User, required = True, reverse_delete_rule=CASCADE)

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()


class Ornaments(Document):
    id = StringField(primary_key = True ,default = lambda: str(uuid4()) )
    id = StringField(primary_key = True ,default = lambda: str(uuid4()) )
    image =  StringField(required = True)
    title = StringField(required = True)
    description = StringField()
    category=ReferenceField(Category, required = True, null=True)
    sharelink = StringField()
    availableon = ListField()
    isSaved = BooleanField()
    
    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class SaveOrnaments(Document):
    id = StringField(primary_key = True ,default = lambda: str(uuid4()) )
    ornaments = ReferenceField(Ornaments, required = True, reverse_delete_rule=CASCADE)
    User = ReferenceField(User, required = True, reverse_delete_rule=CASCADE )

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()


class NailArt(Document):
    
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    category=ReferenceField(Category, required = True, null=True)
    title= StringField(requried =True)
    description = StringField()
    isSaved= BooleanField()
    shareLink= StringField()
    availableOn =ListField()
    image = StringField()

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class SavedNailArt(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    nailArt = ReferenceField( NailArt,required= True ,reverse_delete_rule= CASCADE)
    user = ReferenceField( User, required= True , reverse_delete_rule= CASCADE)

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()


class HairStyle(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    image=StringField(required = True)
    title=StringField(required = True)
    description = StringField(required = True)
    category=ReferenceField(Category, required = True, null=True)
    sharelink = StringField()
    isSaved = BooleanField()
    
    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class SavedHairStyle(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    hairstyle = ReferenceField( HairStyle, required= True ,reverse_delete_rule= CASCADE)
    user = ReferenceField( User, required= True , reverse_delete_rule= CASCADE)

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()

class SelectedItems(Document):
    id = StringField(primary_key = True, default = lambda: str(uuid4()) )
    dress=ReferenceField(Dress)
    ornaments=ReferenceField(Ornaments)
    nailart=ReferenceField(NailArt)
    hairstyle=ReferenceField(HairStyle)

    addedTime = DateTimeField(default=datetime.now())
    updatedTime = DateTimeField()







    