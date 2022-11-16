from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DataTimeField('data published')

class Choice(models.Model):
    question = models.FoerignKey(q)