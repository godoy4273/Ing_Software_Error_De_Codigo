# Generated by Django 2.2.6 on 2020-03-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionadmin', '0013_producto_existenciaminima'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccionCliente',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='direccionEmpleado',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='formapago',
            name='descripcionFormaPago',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='descripcionGarantia',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='descripcionMetodoPago',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccionProveedor',
            field=models.TextField(),
        ),
    ]
