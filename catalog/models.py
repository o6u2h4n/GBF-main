from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True,unique = True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length = 150, db_index=True)
    slug = models.SlugField(max_length = 150, db_index=True, unique = True)
    image = models.ImageField(upload_to='static',blank = True)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField(blank = True)
    availability = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (('id','slug'),)
        verbose_name = "Urun"
        verbose_name_plural = "Urunler"
    
    def __str__(self) -> str:
        return self.name


class Toptext(models.Model):
    name = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True,unique = True)
    date = models.DateField(auto_now=True)


    class Meta:
        ordering = ("name",)
        index_together = (('id','slug'),)
        verbose_name = "Bildirim"
        verbose_name_plural = "Bildirimler"

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.email} tarafından {self.product} ürüne yapılan yorum: {self.body}'
