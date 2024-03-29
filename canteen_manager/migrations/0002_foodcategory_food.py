# Generated by Django 4.2.9 on 2024-01-17 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
        ('canteen_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TimeStamp',
                'verbose_name_plural': 'TimeStamps',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('quantity', models.IntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen_manager.foodcategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TimeStamp',
                'verbose_name_plural': 'TimeStamps',
                'abstract': False,
            },
        ),
    ]
