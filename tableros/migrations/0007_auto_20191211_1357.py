# Generated by Django 2.2.7 on 2019-12-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0006_auto_20191210_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabled',
            name='visibility',
            field=models.CharField(choices=[('Pb', 'Publico'), ('Pr', 'Privado')], max_length=2),
        ),
    ]
