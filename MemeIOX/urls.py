from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'MemeIOX'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)