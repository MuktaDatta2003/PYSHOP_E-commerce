# Generated by Django 4.2.6 on 2023-11-07 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('product_image', models.ImageField(upload_to='product_image/')),
                ('old_prize', models.PositiveIntegerField()),
                ('new_prize', models.PositiveIntegerField()),
                ('quantity', models.IntegerField(max_length=50)),
                ('description', models.TextField(max_length=50)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.catagory')),
            ],
        ),
    ]
