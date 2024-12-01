# Generated by Django 5.1.3 on 2024-11-29 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questify_app', '0006_soal_gambar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulpembelajaran',
            name='deskripsi',
        ),
        migrations.RemoveField(
            model_name='modulpembelajaran',
            name='jumlah_soal',
        ),
        migrations.AlterField(
            model_name='modulpembelajaran',
            name='gratis',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modulpembelajaran',
            name='judul',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='modulpembelajaran',
            name='kategori',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='modulpembelajaran',
            name='kelas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modul', to='questify_app.kelas'),
        ),
        migrations.AlterField(
            model_name='modulpembelajaran',
            name='waktu_pengajaran',
            field=models.IntegerField(help_text='Waktu dalam menit'),
        ),
        migrations.AlterField(
            model_name='soal',
            name='nilai_jawaban',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
