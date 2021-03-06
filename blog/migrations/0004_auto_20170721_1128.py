# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 11:28
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170714_1242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(help_text='글쓴이 이름을 입력해주세요.', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='제목은 간결하게!!', max_length=100, validators=[blog.models.min_length_3]),
        ),
    ]
