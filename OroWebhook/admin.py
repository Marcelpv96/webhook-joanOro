from django.contrib import admin
import models

# Register your models here.
admin.site.register(models.QuestionTopic)
admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.APIAIanswer)
admin.site.register(models.LastQuestion)

