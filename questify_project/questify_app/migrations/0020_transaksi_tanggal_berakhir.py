# Generated by Django 5.1.3 on 2024-12-07 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questify_app', '0019_alter_transaksi_status_pembayaran'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='tanggal_berakhir',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]