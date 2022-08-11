# Generated by Django 4.0.6 on 2022-08-03 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(default='', related_name='posts', to='blogposts.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='images/uploaded_images/bmo.png', null=True, upload_to='uploaded_images/'),
        ),
    ]
