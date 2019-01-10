from mongoengine import Document,StringField,IntField


class Charater(Document):
    name = StringField()
    image = StringField()
    rate = IntField()