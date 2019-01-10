from mongoengine import Document,StringField,IntField

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
