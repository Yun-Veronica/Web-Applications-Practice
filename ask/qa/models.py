from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-pk')
    
  def popular(self):
    return self.order_by('-rating')

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank = True, auto_now_add=True)
  rating = models.IntegerField(default = 0)
  author = models.ForeignKey(User)
  likes  = models.ManyToManyField(User, related_name='users_likes')
  objects = QuestionManager()

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return '/question/%d/' %self.pk
    
  def questionID(self):
    return  self.pk
    

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField()
  author = models.ForeignKey(User)
  question = models.ForeignKey(Question)
   
  def __str__(self):
      return self.text
  
  def get_absolute_url(self):
      return '/answer/%d/' %self.pk


