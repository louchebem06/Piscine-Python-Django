# Generated by Django 4.0.5 on 2022-06-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('repassword', models.CharField(max_length=100)),
            ],
        ),
    ]