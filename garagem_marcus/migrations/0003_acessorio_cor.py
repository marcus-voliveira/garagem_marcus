# Generated by Django 4.1.7 on 2023-04-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem_marcus', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrição', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrição', models.CharField(max_length=100)),
            ],
        ),
    ]