# Generated by Django 3.0.5 on 2020-05-18 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20200516_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Psychologist_User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Users.User')),
                ('practitioners_id', models.CharField(max_length=255, null=True)),
                ('practice_address', models.CharField(max_length=255, null=True)),
                ('practice_work_number', models.CharField(max_length=255, null=True)),
                ('practice_email', models.CharField(max_length=255, null=True)),
            ],
            bases=('Users.user',),
        ),
        migrations.CreateModel(
            name='Patient_User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Users.User')),
                ('diagnosis_id', models.CharField(max_length=255, null=True)),
                ('psychologist_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Psychologist_User')),
            ],
            bases=('Users.user',),
        ),
    ]
