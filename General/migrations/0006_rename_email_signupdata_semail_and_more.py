# Generated by Django 5.0.3 on 2024-03-26 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0005_signupdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdata',
            old_name='email',
            new_name='semail',
        ),
        migrations.RenameField(
            model_name='signupdata',
            old_name='password',
            new_name='spassword',
        ),
        migrations.RenameField(
            model_name='signupdata',
            old_name='username',
            new_name='susername',
        ),
    ]
