# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OroWebhook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='AnswerA',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='AnswerB',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='AnswerC',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='QuestionTopic',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='QuestionTopic',
        ),
    ]
