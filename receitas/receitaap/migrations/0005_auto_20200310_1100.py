# Generated by Django 2.1.15 on 2020-03-10 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitaap', '0004_receitas_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receitas',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]