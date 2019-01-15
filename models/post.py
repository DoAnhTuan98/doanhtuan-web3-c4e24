from mongoengine import Document, StringField, ReferenceField

class Post(Document):
    title = StringField()
    content = StringField()
    owner = ReferenceField("User")
    