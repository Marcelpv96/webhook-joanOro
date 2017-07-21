from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    Question = models.TextField(null=False)
    QuestionTopic = models.TextField(null=True)
    def __unicode__(self):
        return u'{0}'.format(self.Question)

class Answer(models.Model):
    Question = models.ForeignKey(Question)
    Answer = models.TextField(null=False)

    def  __unicode__(self):
        return u'{0}'.format(self.Answer)

class BadAnswer(models.Model):
    Answer = models.TextField(null=False)

    def  __unicode__(self):
        return u'{0}'.format(self.Answer)

class APIAIanswer(models.Model):
    speech = models.TextField(null=True)
    displayText = models.TextField(null=True)
    source = models.CharField(max_length=20, default='Webhook-JoanOro', editable=False)

    def __unicode__(self):
        return u'{0}'.format(self.speech)


