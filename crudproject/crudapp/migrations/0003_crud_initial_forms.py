# Generated by Django 4.1.2 on 2022-10-18 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crudapp", "0002_crud_total_forms_alter_crud_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="crud",
            name="INITIAL_FORMS",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
