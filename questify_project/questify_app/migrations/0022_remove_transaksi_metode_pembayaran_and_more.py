# Generated by Django 5.1.3 on 2024-12-11 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questify_app', '0021_remove_transaksi_tanggal_berakhir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksi',
            name='metode_pembayaran',
        ),
        migrations.DeleteModel(
            name='MetodePembayaran',
        ),
    ]
