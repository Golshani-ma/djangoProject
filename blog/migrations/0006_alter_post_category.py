# Generated by Django 4.2.8 on 2024-01-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_alter_post_image_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(null=True, to='blog.category'),
        ),
    ]
