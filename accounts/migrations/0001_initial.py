# Generated by Django 3.2.3 on 2021-05-30 07:01

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(max_length=200)),
                ('fathername', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=50)),
                ('DOB', models.DateField(default='1998-01-01')),
                ('role', models.CharField(choices=[('Intern', 'Inter'), ('Software_Engineer', 'Software_Engineer'), ('Senior_Engineer', 'Senior_Engineer'), ('Manager', 'Manager'), ('Executive', 'Executive')], max_length=100)),
                ('dept', models.CharField(choices=[('HR', 'HR'), ('Sales', 'Sales'), ('Cloud', 'Cloud'), ('AI', 'AI'), ('Devops', 'Devops'), ('Backend', 'Backend'), ('UI', 'UI'), ('QA', 'QA')], max_length=100)),
            ],
            options={
                'db_table': 'employee',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'db_table': 'system',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(default='2021-05-26')),
                ('enddate', models.DateField(default='2021-05-26')),
                ('name', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Declined', 'Declined'), ('Wait', 'Wait')], default='Wait', max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]