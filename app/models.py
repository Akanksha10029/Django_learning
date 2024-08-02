from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('Bk', 'Black'),
        ('Gr', 'Ginger'),
        ('Kl', 'Kiwi'),
        ('Ms', 'Masala'),
        ('Pl', 'Plain'),  
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='chai_varieties/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    
    def __str__(self):
        return self.name