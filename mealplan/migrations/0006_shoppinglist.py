# Generated by Django 4.2.7 on 2023-12-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealplan', '0005_alter_ingredient_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ManyToManyField(to='mealplan.ingredient')),
            ],
        ),
    ]
