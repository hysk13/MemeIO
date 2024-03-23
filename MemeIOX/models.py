from django.db import models
# Create your models here.
class Topic(models.Model):

    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topics'

    def __str__(self):
        return self.title

class Entry(models.Model):

    title = models.CharField(max_length=300, null=True)
    entry_file = models.ImageField(null=True, default="https://placehold.co/500x500")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.title[:50]