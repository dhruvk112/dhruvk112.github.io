# Generated by Django 3.1.1 on 2020-10-04 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20201003_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='person1',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='person2',
            field=models.CharField(max_length=128),
        ),
    ]