# Generated by Django 3.1.4 on 2020-12-10 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='assignee',
            name='first_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='assignee',
            name='last_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(related_name='author_tasks', to='app.Assignee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_tasks', to='app.author'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_edited',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
