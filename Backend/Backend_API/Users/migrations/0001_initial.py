# Generated by Django 3.0.5 on 2020-04-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, null=True)),
                ('email_address', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('tile', models.CharField(max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True)),
                ('cell_number', models.CharField(max_length=255, null=True)),
                ('date_of_birth', models.DateTimeField(auto_now=True, null=True)),
                ('gender', models.CharField(max_length=255, null=True)),
                ('primary_address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('postal_code', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('citizenship', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
