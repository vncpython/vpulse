# Generated by Django 3.0.2 on 2020-02-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_physiotherapist'),
    ]

    operations = [
        migrations.CreateModel(
            name='specilization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
            ],
        ),
    ]