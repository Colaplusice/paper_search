# Generated by Django 3.1.6 on 2021-02-10 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0006_wordposition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordposition',
            old_name='paper_id',
            new_name='paper',
        ),
    ]