# Generated by Django 4.0.6 on 2022-08-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0004_ponto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponto',
            name='dados',
            field=models.TextField(),
        ),
    ]
