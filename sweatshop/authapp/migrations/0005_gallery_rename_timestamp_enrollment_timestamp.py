# Generated by Django 4.2.11 on 2025-04-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_membershipplan_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='timeStamp',
            new_name='TimeStamp',
        ),
    ]
