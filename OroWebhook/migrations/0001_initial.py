# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Answer', models.TextField()),
                ('Letter', models.TextField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='APIAIanswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speech', models.TextField(null=True)),
                ('displayText', models.TextField(null=True)),
                ('source', models.CharField(default=b'Webhook-JoanOro', max_length=20, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='BadAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='lastQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAndCorrect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CorrectAnswer', models.ForeignKey(to='OroWebhook.Answer')),
                ('Question', models.ForeignKey(to='OroWebhook.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('QuestionTopic', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='QuestionTopic',
            field=models.ForeignKey(to='OroWebhook.QuestionTopic'),
        ),
        migrations.AddField(
            model_name='lastquestion',
            name='question',
            field=models.ForeignKey(to='OroWebhook.Question'),
        ),
        migrations.AddField(
            model_name='badanswer',
            name='Question',
            field=models.ForeignKey(to='OroWebhook.Question'),
        ),
    ]
