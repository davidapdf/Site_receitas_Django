# Generated by Django 2.1.15 on 2020-03-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitaap', '0002_receitas_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receitas',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
