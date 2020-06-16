# Generated by Django 3.0.7 on 2020-06-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
                ('image_name', models.CharField(max_length=200, null=True)),
                ('_type', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]