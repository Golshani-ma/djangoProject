# Generated by Django 4.2.8 on 2024-01-01 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelTableComment(
            name='contact',
            table_comment='Contact Table Commentssssssssss',
        ),
    ]
