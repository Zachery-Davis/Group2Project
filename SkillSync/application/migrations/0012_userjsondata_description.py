# Generated by Django 5.1.3 on 2024-12-02 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0011_userjsondata"),
    ]

    operations = [
        migrations.AddField(
            model_name="userjsondata",
            name="description",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]