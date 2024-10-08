# Generated by Django 4.2.6 on 2024-09-30 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_alter_case_litigant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='address',
            field=models.TextField(blank=True, default='Address not provided', null=True),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='specialty',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='case',
            name='advocate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advocate_cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='case',
            name='court_staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='case',
            name='litigant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='litigant_cases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='case',
            name='title',
            field=models.CharField(default='Law', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_permissions', to='auth.permission'),
        ),
    ]
