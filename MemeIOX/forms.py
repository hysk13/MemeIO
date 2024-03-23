from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
        exclude = ['topic']