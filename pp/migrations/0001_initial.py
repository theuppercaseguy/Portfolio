# Generated by Django 4.0.4 on 2022-11-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviewsss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('linkedin', models.TextField()),
                ('priority', models.IntegerField()),
                ('title', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]
