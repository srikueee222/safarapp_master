# Generated by Django 3.0.5 on 2020-07-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=1024)),
                ('refresh_token', models.CharField(max_length=1024)),
                ('access_token_created_at', models.DateTimeField(auto_now_add=True)),
                ('refresh_token_created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]