# Generated by Django 3.0.5 on 2020-05-16 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='User_Roles',
            fields=[
                ('user_role_id', models.AutoField(primary_key=True, serialize=False)),
                ('roleid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Roles')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.User')),
            ],
        ),
    ]
