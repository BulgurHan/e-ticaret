# Generated by Django 4.0.3 on 2022-04-07 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='İsim')),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='İsim')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Açıklama')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tutar')),
                ('image', models.ImageField(blank=True, upload_to='product', verbose_name='Resim')),
                ('stock', models.IntegerField()),
                ('avaible', models.BooleanField(default=False, verbose_name='Görünür')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
                'ordering': ('name',),
            },
        ),
    ]
