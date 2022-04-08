from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        verbose_name = 'İsim'
    )
    slug = models.SlugField(
        max_length = 250,
        unique = True,
    )
    class Meta:
        ordering = ('name',)
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return "{}".format(self.name)



class Product(models.Model):
    name = models.CharField(
        max_length = 250,
        unique = True,
        verbose_name = 'İsim'
    )
    slug = models.SlugField(
        max_length = 250,
        unique = True
    )
    description = models.TextField(
        blank = True,
        verbose_name = 'Açıklama'
    )
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE
    )
    price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        verbose_name = 'Tutar'
    )
    image = models.ImageField(
        upload_to = 'product',
        blank = True,
        verbose_name = 'Resim'
    )
    stock = models.IntegerField()
    avaible = models.BooleanField(
        default = False,
        verbose_name = 'Görünür'
    )
    created = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Oluşturulma Tarihi'
    )
    updated = models.DateTimeField(
        auto_now = True,
        verbose_name = 'Güncellenme Tarihi'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
    def get_url(self):
        return reverse('ProdCatDetail', args=[self.category.slug, self.slug])
    def __str__(self):
        return "{}".format(self.name)