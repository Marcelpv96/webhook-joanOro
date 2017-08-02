from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    Question = models.TextField(null=False)
    AnswerA = models.TextField(null=False)
    AnswerB = models.TextField(null=False)
    AnswerC = models.TextField(null=False)
    Correct = models.TextField(null=False)
    QuestionTopic = models.TextField(null=False)

    def __unicode__(self):
        return u'{0}'.format("the question is: "+self.Question+" |a,b,c| "+self.QuestionTopic)

class APIAIanswer(models.Model):
    question = models.ForeignKey(Question,null=False)
    speech = models.TextField(null=True)
    displayText = models.TextField(null=True)
    source = models.CharField(max_length=20, default='Webhook-JoanOro', editable=False)

    def __unicode__(self):
        return u'{0}'.format(self.speech)

class LastQuestion(models.Model):
    question = models.ForeignKey(Question,null=False)

    def correct(self):
        return str(self.question.Correct)

    def __str__(self):
        return u'{0}'.format(self.question.Question+" |Correct answer >>| ")
    def __unicode__(self):
        return u'{0}'.format(self.question.Question+" |Correct answer >>| ")
