from ninja import Schema, ModelSchema
from datetime import date
from .models import Note


class CategoryIn(Schema):
    title: str
    description: str

class CategoryOut(Schema):
    id: int
    title: str
    description: str    
    created: date
  

class NoteIn(ModelSchema):
    class Config:
        model = Note
        model_fields = ['title', 'category']

class NoteUpd(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'completed']

class NoteOut(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id','title', 'category', 'created', 'completed']