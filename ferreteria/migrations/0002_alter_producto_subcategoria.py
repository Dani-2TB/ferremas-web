# Generated by Django 4.2.6 on 2024-05-21 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='subcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ferreteria.subcategoria', verbose_name='Subategoría'),
        ),
    ]