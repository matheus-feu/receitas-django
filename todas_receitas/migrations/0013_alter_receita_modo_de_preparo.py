# Generated by Django 4.1.2 on 2022-10-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todas_receitas', '0012_alter_receita_modo_de_preparo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='modo_de_preparo',
            field=models.TextField(),
        ),
    ]
