from datetime import date
from typing import List
from ninja import NinjaAPI, Schema
from django.shortcuts import get_object_or_404
from .models import Note, Category
from .schemas import NoteIn, NoteOut, NoteUpd, CategoryIn, CategoryOut


api = NinjaAPI()


@api.post("/notes", tags=['Заметки'])
def create_note(request, payload: NoteIn):
    data = payload.dict()
    category = Category.objects.get(id=data['category'])
    del data['category']
    note = Note.objects.create(category=category, **data)
    return {"id": note.id}

@api.post("/category", tags=['Категории'])
def create_category(request, payload: CategoryIn):
    category = Category.objects.create(**payload.dict())
    return {"id":category.id}    


@api.get("/notes/{note_id}", response=NoteOut, tags=['Заметки'])
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note

@api.get("/category/{category_id}", response=CategoryOut, tags=['Категории'])
def get_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return category

@api.get("/category", response=List[CategoryOut], tags=['Категории'])
def list_categories(request):
    categories = Category.objects.all()
    return categories   

@api.get("/notes", response=List[NoteOut], tags=['Заметки'])
def list_notes(request):
    notes = Note.objects.all()
    return notes


@api.patch("/notes/{note_id}", tags=['Заметки'])
def update_note(request, note_id: int, payload: NoteUpd):
    note = get_object_or_404(Note, id=note_id)
    for attr, value in payload.dict().items():
        setattr(note, attr, value)
    note.save()
    return {"success": True}

@api.put("/category/{category_id}", tags=['Категории'])
def update_category(request, category_id: int, payload: CategoryIn):
    note = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(note, attr, value)
    category.save()
    return {"success": True}

@api.delete("/notes/{note_id}", tags=['Заметки'])
def delete_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return {"success": True}

@api.delete("/category/{category_id}", tags=['Категории'])
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}