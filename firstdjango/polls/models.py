from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone

# this is the model for the question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    # define a method to provide default __str__ to Django
    def __str__(self):
        return self.question_text
        
    # method for checking if question was recently published
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# each question has choices
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    # method to provide default __str__ to Django
    def __str__(self):
        return self.choice_text

