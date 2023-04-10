# Generated by Django 4.1.7 on 2023-04-10 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem_marcus', '0003_acessorio_cor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cor',
            new_name='Core',
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(default=0, max_length=4, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Veiculos', to='garagem_marcus.categoria')),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Veiculos', to='garagem_marcus.core')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Veiculos', to='garagem_marcus.marca')),
            ],
        ),
    ]