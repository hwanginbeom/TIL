# Generated by Django 3.1.1 on 2020-09-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('user_pwd', models.CharField(max_length=50)),
                ('uswer_nmae', models.CharField(max_length=50)),
            ],
        ),
    ]
