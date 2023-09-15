from mongoengine import Document, StringField, EmailField, IntField, DateTimeField,\
    ListField, EmbeddedDocumentField, EmbeddedDocument


class Medication(EmbeddedDocument):
    name = StringField(required=True)
    # dosage = StringField(required=True)
    time = StringField(required=True)
    duration = StringField(required=True)


class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    dob = DateTimeField(required=True)
    phone = StringField(required=True)
    gender = StringField(required=True)
    medications = ListField(EmbeddedDocumentField(Medication))
