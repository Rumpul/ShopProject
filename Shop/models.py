from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка категории')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url_shop(self):
        return reverse('Shop:product_list_by_category',
                       args=[self.slug])

    def get_absolute_url_reviews(self):
        return reverse('reviews:reviews_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка товара')
    main_image = models.ImageField(upload_to='products_image/%Y/%m/%d', blank=True, verbose_name='Фото')
    video = models.FileField(upload_to='products_video/%Y/%m/%d', blank=True, verbose_name='Видео')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество товара на складе')
    available = models.BooleanField(default=True, verbose_name='Доступность товара')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url_shop(self):
        return reverse('Shop:product_detail',
                       args=[self.id, self.slug])

    def get_absolute_url_reviews(self):
        return reverse('reviews:review_detail',
                       args=[self.id, self.slug])


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product_all_images/%Y/%m/%d')  # здесь укажите куда сохранять изображения
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
