# Generated by Django 3.0.5 on 2020-05-23 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20200523_1452'),
        ('Activities', '0002_auto_20200522_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Types',
            fields=[
                ('activity_type', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assigned_Activities',
            fields=[
                ('assigned_activities', models.AutoField(primary_key=True, serialize=False)),
                ('due_date', models.DateTimeField(blank=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('isCompleted', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proof_Activities',
            fields=[
                ('proof', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('pathname', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proof_Activities_Type',
            fields=[
                ('proof_type', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='activities',
            old_name='activity_id',
            new_name='activity',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='patient_activities',
        ),
        migrations.AddField(
            model_name='activities',
            name='activity_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Completed_Activities',
            fields=[
                ('completed_activities', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Activities.Assigned_Activities')),
                ('completion_date', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('proof', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Activities.Proof_Activities')),
            ],
        ),
        migrations.DeleteModel(
            name='Activity_Proof',
        ),
        migrations.AddField(
            model_name='assigned_activities',
            name='activity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Activities.Activities'),
        ),
        migrations.AddField(
            model_name='assigned_activities',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Users.Patient_User'),
        ),
        migrations.AddField(
            model_name='activities',
            name='proof_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Activities.Proof_Activities_Type'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Activities.Activity_Types'),
        ),
    ]
