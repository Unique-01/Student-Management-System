# Generated by Django 4.2.5 on 2023-09-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0003_rename_code_department_department_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculationNumberCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_generated_number', models.IntegerField(default=0)),
            ],
        ),
    ]