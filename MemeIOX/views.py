from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from datetime import datetime

# Create your views here.
def index(req):
    topics = Topic.objects.order_by('-date_added')
    ctx = {'topics': topics}
    return render(req, 'index.html', ctx)

def topics(req):
    topics = Topic.objects.order_by('-date_added')
    ctx = {'topics': topics}
    return render(req, 'topics.html', ctx)

def new_topic(req):
    if req.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=req.POST)
        if form.is_valid():
            create_topic = form.save(commit=False)
            create_topic.save()
            print('Success!')
            return redirect('MemeIOX:topics')
    ctx = {'form': form}
    return render(req, 'new_topic.html', ctx)

def topic(req, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = Entry.objects.filter(topic=topic_id).order_by('-date_added')
    ctx = {'topic': topic, 'entries': entries}
    return render(req, 'topic.html', ctx)

def new_entry(req, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if req.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(req.POST, req.FILES)
        if form.is_valid():
            create_entry = form.cleaned_data
            Entry.objects.create(title=create_entry['title'], entry_file=create_entry['entry_file'], topic=Topic.objects.get(id=topic_id), date_added=datetime.now())
            return redirect('MemeIOX:topic', topic_id)
    ctx = {'topic': topic, 'form' : form}
    return render(req, 'new_entry.html', ctx)