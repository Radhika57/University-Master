# Generated by Django 4.1.3 on 2023-03-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_student_result"),
    ]

    operations = [
        migrations.AlterField(
            model_name="university",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
