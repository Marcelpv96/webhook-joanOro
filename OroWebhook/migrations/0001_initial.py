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
            name='LastQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Question', models.TextField()),
                ('Correct', models.TextField()),
                ('AnswerA', models.ForeignKey(related_name='answer_a', to='OroWebhook.Answer')),
                ('AnswerB', models.ForeignKey(related_name='answer_b', to='OroWebhook.Answer')),
                ('AnswerC', models.ForeignKey(related_name='answer_c', to='OroWebhook.Answer')),
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
            model_name='apiaianswer',
            name='question',
            field=models.ForeignKey(to='OroWebhook.Question'),
        ),
    ]
