# Generated by Django 3.1.1 on 2020-10-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20201003_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='person1',
            field=models.CharField(choices=[(1, 'Danielle Clayton'), (2, 'Robert Bailey'), (3, 'Benjamin Reeves'), (4, 'Shelley French'), (5, 'Stacy Stanley'), (6, 'Vanessa Fitzpatrick'), (7, 'Daniel Williams'), (8, 'Holly Powell'), (9, 'Kristie Ramos'), (10, 'William Morris')], max_length=128),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='person2',
            field=models.CharField(choices=[(1, 'Danielle Clayton'), (2, 'Robert Bailey'), (3, 'Benjamin Reeves'), (4, 'Shelley French'), (5, 'Stacy Stanley'), (6, 'Vanessa Fitzpatrick'), (7, 'Daniel Williams'), (8, 'Holly Powell'), (9, 'Kristie Ramos'), (10, 'William Morris')], max_length=128),
        ),
    ]
