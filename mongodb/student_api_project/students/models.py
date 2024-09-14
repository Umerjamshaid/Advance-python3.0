from mongoengine import Document, StringField, IntField

class Students(Document):
    student_id = IntField(required=True, unique=True)
    name = StringField(max_length=200, required=True)
    which_class = IntField(required=True)
    age = IntField(required=True)

    def __str__(self):
        return self.name
