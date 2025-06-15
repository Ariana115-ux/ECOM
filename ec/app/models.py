from django.db import models

# Create your models here.


CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-creams'),
    
)










class Product(models.Model):
    title=models.Charfield(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default=' ')
    prodapp  = models.TextField(default=' ')
    category = models.CharField(choices=CATEGORY CHOICES,max_length=2)
    product_image  = models.ImageField(upload_to='produt')
  
    def__str__(self):
    return self.title