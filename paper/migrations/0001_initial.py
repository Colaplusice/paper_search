# Generated by Django 3.1.5 on 2021-02-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('paper_title', models.TextField(verbose_name='Paper Name')),
                ('authors', models.TextField(verbose_name='author')),
                ('year', models.DateTimeField(verbose_name='time')),
                ('publication_venue', models.CharField(max_length=255, null=True, verbose_name='venue')),
                ('abstract', models.TextField(verbose_name='abstract')),
                ('n_citation', models.IntegerField(verbose_name='citation')),
                ('references', models.TextField(verbose_name='references')),
            ],
        ),
    ]
