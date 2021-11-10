from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField()
  rating = models.IntegerField()
  author = models.CharField(max_length=50)
  likes  = models.ForeignKey(User)
  
  def __unicode__(self):
    return self.title
  
  def get_absolute_url(self):
    return '/question/%d/' %self.pk
    
  def questionID(self):
    return  self.pk
    

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  author = models.CharField(max_length=50)
  question = models.OnetoOneField(Question)
   
    def __unicode__(self):
        return self.title
  
    def get_absolute_url(self):
        return '/answer/%d/' %self.pk


class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('added_at')[:20]
    
  def popular(self):
    return self.order_by('rating')
