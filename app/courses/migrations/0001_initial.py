# Generated by Django 3.1.6 on 2021-03-05 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название курса')),
                ('description', models.TextField(verbose_name='описание курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_number', models.PositiveSmallIntegerField(default=1, verbose_name='порядковый номер занятия')),
                ('topic', models.CharField(max_length=100, verbose_name='тема занятия')),
                ('summary', models.TextField(blank=True, verbose_name='содержание занятия')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'занятие',
                'verbose_name_plural': 'занятия',
                'ordering': ['seq_number'],
            },
        ),
    ]
