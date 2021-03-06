# Generated by Django 3.0.2 on 2020-02-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200203_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gynecologist',
            fields=[
                ('Disease', models.CharField(choices=[('Amenorrhea', 'Amenorrhea'), ('Endometriosis', 'Endometriosis'), ('Menstrual Disorders', 'Menstrual Disorders'), ('Pelvic Pain', 'Pelvic Pain'), ('Uterine Fibroids', 'Uterine Fibroids')], max_length=250, primary_key=True, serialize=False)),
                ('Patient_id', models.CharField(max_length=250)),
                ('Consultant', models.CharField(choices=[('Charles R Drew', 'Charles R Drew'), ('Michael Debakey', 'Michael Debakey'), ('Gazi Yasargill', 'Gazi Yasargill'), ('Zeki Uygur', 'Zeki Uygur'), ('Ariadna Gil', 'Ariadna Gil'), ('Daisy Sylvie', 'Daisy Sylvie'), ('Samantha Haggo', 'Samantha Haggo'), ('Olivia Rae', 'Olivia Rae'), ('Svyatoslav Fyodorov', 'Svyatoslav Fyodorov'), ('Vera Gedroits', 'Vera Gedroits'), ('Mariel Pontigon', 'Mariel Pontigon'), ('Leo Soriano', 'Leo Soriano'), ('Tony Ura', 'Tony Ura'), ('Dogodo Bau', 'Dogodo Bau'), ('Noor Ali Zadran', 'Noor Ali Zadran'), ('Gulbadin Naib', 'Gulbadin Naib'), ('Masazumi Harada', 'Masazumi Harada'), ('Hanaoka Seishu', 'Hanaoka Seishu'), ('Sushmitha Sinha', 'Sushmitha Sinha'), ('Parvathi Nambiyaar', 'Parvathi Nambiyaar'), ('Hermann Von Helmholtz', 'Hermann Von Helmholtz'), ('Maria Furtwangler', 'Maria Furtwangler'), ('Katherine Brun', 'Katherine Brun'), ('Georgia Elwiss', 'Georgia Elwiss'), ('Celia Cruz', 'Celia Cruz'), ('Elizabeth Pena', 'Elizabeth Pena'), ('Ji Ben', 'Ji Ben'), ('Ge Hong', 'Ge Hong'), ('Vera Peters', 'Vera Peters'), ('Augusta Cohen', 'Augusta Cohen'), ('Raquel Muniz', 'Raquel Muniz'), ('Francisca Praguer', 'Francisca Praguer'), ('James Graham', 'James Graham'), ('Alex Carey', 'Alex Carey'), ('Stefan Swanpoel', 'Stefan Swanpoel'), ('Riaan Walters', 'Riaan Walters')], max_length=250)),
            ],
        ),
    ]
