# Generated by Django 2.2.6 on 2020-04-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0106_auto_20200409_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Fecha',
            field=models.DateTimeField(),
        ),
    ]