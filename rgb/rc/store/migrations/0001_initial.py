# Generated by Django 2.1.2 on 2018-10-31 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=20, verbose_name='CATEGORY')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=20, verbose_name='LOCATION')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='NAME')),
                ('description', models.TextField(verbose_name='DESCRIPTION')),
                ('img', models.CharField(max_length=100, verbose_name='IMG')),
                ('status', models.CharField(default='Y', max_length=1, verbose_name='STATUS')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Location')),
            ],
        ),
    ]
