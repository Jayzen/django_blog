# Generated by Django 4.1.2 on 2022-10-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article", name="content", field=models.TextField(),
        ),
    ]
