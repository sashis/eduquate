# Generated by Django 3.1.6 on 2021-02-15 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('accounts', '0001_initial'),
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', through='learning.CourseSubscription', to='accounts.Student', verbose_name='студенты'),
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.tutor', verbose_name='преподаватель'),
        ),
    ]
