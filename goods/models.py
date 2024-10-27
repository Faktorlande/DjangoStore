from django.db import models
from django.template.defaulttags import verbatim

# Create your models here.


class Categories(models.Model):


    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')


    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Products(models.Model):

    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    slug = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='goods_images', null=True, blank=True, verbose_name="Изображение")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена", default=0.00)
    discount = models.IntegerField(default=0, verbose_name="Скидка в %")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")


    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"

