# Generated by Django 4.0.5 on 2022-06-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petfinder', '0004_remove_profile_image_post_active_post_available_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='bio',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_three',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_two',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=500, upload_to=''),
        ),
    ]
