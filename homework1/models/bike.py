from mongoengine import Document, StringField,IntField

class Bike(Document):
    model = StringField()
    daily = IntField()
    image = StringField()
    year = StringField()
