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
    AnswerA = models.ForeignKey(Answer,related_name="answer_a",null=False)
    AnswerB = models.ForeignKey(Answer,related_name="answer_b",null=False)
    AnswerC = models.ForeignKey(Answer,related_name="answer_c",null=False)
    Correct = models.TextField(null=False)
    QuestionTopic = models.ForeignKey(QuestionTopic,null=False)

    def generateSpeech(self):
        return "The question is :"+self.Question+" options:"+self.AnswerA+" "+self.AnswerB+" "+self.AnswerC

    def __unicode__(self):
        return u'{0}'.format(self.Question+" |a,b,c| "+self.QuestionTopic)

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
        return self.question.Correct
    def __unicode__(self):
        return u'{0}'.format(self.question.Question+" |Correct answer >>| ")
