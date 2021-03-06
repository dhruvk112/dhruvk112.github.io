# Generated by Django 3.1.1 on 2020-10-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=256)),
                ('date_of_birth', models.DateField(max_length=128)),
                ('balance', models.FloatField(max_length=10)),
            ],
        ),
    ]
