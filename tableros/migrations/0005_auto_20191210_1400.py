# Generated by Django 2.2.7 on 2019-12-10 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tableros', '0004_auto_20191210_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabled',
            name='dueno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_dueno', to=settings.AUTH_USER_MODEL),
        ),
    ]
