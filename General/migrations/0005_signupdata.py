# Generated by Django 5.0.3 on 2024-03-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0004_productmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='signupdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
