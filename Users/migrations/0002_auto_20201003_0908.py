# Generated by Django 3.1.1 on 2020-10-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person1', models.CharField(max_length=128)),
                ('person2', models.CharField(max_length=128)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='balance',
            field=models.FloatField(),
        ),
    ]