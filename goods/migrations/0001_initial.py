# Generated by Django 4.2.8 on 2024-10-27 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Цена')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка в %')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product',
            },
        ),
    ]
