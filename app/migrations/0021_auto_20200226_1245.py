# Generated by Django 3.0.2 on 2020-02-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_pharmacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='PharmacyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specialization', models.CharField(max_length=300)),
                ('Disease', models.CharField(max_length=300)),
                ('Medication', models.CharField(max_length=300)),
                ('In_Stock', models.CharField(max_length=300)),
                ('Out_Stock', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Pharmacy',
        ),
    ]
