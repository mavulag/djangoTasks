# Generated by Django 4.2.7 on 2023-11-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task_title', models.CharField(max_length=100)),
                ('task_details', models.TextField()),
            ],
        ),
    ]
