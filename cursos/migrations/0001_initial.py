# Generated by Django 3.0.5 on 2020-04-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('sigla', models.CharField(max_length=5)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
