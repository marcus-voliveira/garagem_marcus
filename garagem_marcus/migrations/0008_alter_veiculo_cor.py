# Generated by Django 4.1.7 on 2023-05-19 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem_marcus', '0007_rename_cor_veiculo_cor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Cor', to='garagem_marcus.cor'),
        ),
    ]