# Generated by Django 3.2.14 on 2022-07-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ingridient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingridients',
            field=models.ManyToManyField(to='core.Ingridient'),
        ),
    ]
