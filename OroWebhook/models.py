from django.db import models
from django.utils import timezone

# Create your models here.

class QuestionTopic(models.Model):
    QuestionTopic = models.TextField(null=False)
    def __unicode__(self):
        return u'{0}'.format(self.QuestionTopic)

class Answer(models.Model):
    Answer = models.TextField(null=False)
    Letter = models.TextField(max_length=1,null=False)
    def  __unicode__(self):
        return u'{0}'.format(self.Answer)

class Question(models.Model):
    Question = models.TextField(null=False)
    QuestionTopic = models.ForeignKey(QuestionTopic,null=False)
    def __unicode__(self):
        return u'{0}'.format(self.Question+" || "+self.QuestionTopic)

class QuestionAndCorrect(models.Model):
    Question = models.ForeignKey(Question,null=False)
    CorrectAnswer = models.ForeignKey(Answer,null=False)
    def __unicode__(self):
        return u'{0}'.format(self.Question.Question+" <<Correct answer>> "+self.CorrectAnswer.Answer)


class BadAnswer(models.Model):
    Question = models.ForeignKey(Question,null=False)
    Answer = models.TextField(null=False)

    def  __unicode__(self):
        return u'{0}'.format(self.Answer)

class APIAIanswer(models.Model):
    speech = models.TextField(null=True)
    displayText = models.TextField(null=True)
    source = models.CharField(max_length=20, default='Webhook-JoanOro', editable=False)

    def __unicode__(self):
        return u'{0}'.format(self.speech)

class lastQuestion(models.Model):
    question = models.ForeignKey(Question,null=False)

    def __unicode__(self):
        return u'{0}'.format(self.question.Question+" |Correct answer >>| ")
