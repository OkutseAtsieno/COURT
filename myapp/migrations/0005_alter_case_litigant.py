# Generated by Django 4.2.6 on 2024-09-21 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_case_options_remove_advocate_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='litigant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='litigant_cases', to='myapp.customuser'),
        ),
    ]
