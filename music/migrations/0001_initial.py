# Generated by Django 3.2 on 2021-04-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('prefix', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('label', models.CharField(max_length=200)),
                ('ASIN', models.CharField(max_length=10)),
                ('released_date', models.DateField(blank=True, null=True)),
                ('cover_image', models.ImageField(upload_to='cover_image')),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.band')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.band'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ManyToManyField(to='music.Genre'),
        ),
    ]
