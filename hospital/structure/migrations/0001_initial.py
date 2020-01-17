# Generated by Django 3.0.2 on 2020-01-17 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('short_title', models.CharField(max_length=20)),
                ('tel1', models.CharField(max_length=15)),
                ('tel2', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='structure/logo/')),
                ('about', models.TextField(blank=True, null=True)),
                ('history', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Больница',
                'verbose_name_plural': 'Больницы',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='structure/offices/')),
                ('about', models.TextField(blank=True, null=True)),
                ('history', models.TextField(blank=True, null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='structure.Hospital')),
            ],
            options={
                'verbose_name': 'Отделение',
                'verbose_name_plural': 'Отделения',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='structure/departments/')),
                ('about', models.TextField(blank=True, null=True)),
                ('history', models.TextField(blank=True, null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='structure.Hospital')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='structure.Office')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
                'ordering': ('-title',),
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=10)),
                ('tel', models.CharField(blank=True, max_length=15, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='hospital/offices/departments/cabinets/%m/')),
                ('about', models.TextField(blank=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cabinets', to='structure.Department')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinets', to='structure.Hospital')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cabinets', to='structure.Office')),
            ],
        ),
    ]