# Generated by Django 3.0.3 on 2020-02-26 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_file', models.FileField(upload_to=None)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturers_feed.Brand')),
            ],
        ),
    ]
