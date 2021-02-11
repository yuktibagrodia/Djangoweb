from tastypie.resources import ModelResource
from django.db import models
from django import forms
from .models import Note
from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization=Authorization()
        fields=['question','option1','option2','option3','answer']