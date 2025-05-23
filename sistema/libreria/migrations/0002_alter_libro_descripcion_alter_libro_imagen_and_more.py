# Generated by Django 4.1.13 on 2025-03-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='libros/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
