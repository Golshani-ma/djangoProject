# Generated by Django 4.2.8 on 2024-01-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_newsletter_alter_contact_table_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]