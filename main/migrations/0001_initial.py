# Generated by Django 5.2 on 2025-04-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='icons/')),
                ('review', models.TextField()),
                ('screenshots', models.JSONField(blank=True, default=list)),
                ('download_link_1', models.URLField(blank=True, max_length=500, null=True)),
                ('download_link_2', models.URLField(blank=True, max_length=500, null=True)),
                ('download_link_3', models.URLField(blank=True, max_length=500, null=True)),
                ('pros', models.JSONField(blank=True, default=list)),
                ('cons', models.JSONField(blank=True, default=list)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
