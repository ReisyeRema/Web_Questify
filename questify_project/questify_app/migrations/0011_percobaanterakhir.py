# Generated by Django 5.1.3 on 2024-11-30 11:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questify_app', '0010_alter_modulpembelajaran_deskripsi_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PercobaanTerakhir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percobaan_ke', models.IntegerField(default=1)),
                ('modul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questify_app.modulpembelajaran')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
