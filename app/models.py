from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description = models.TextField(default="empty")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='chai_varieties/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    
    def __str__(self):
        return self.name

# one to many
    
class ChaiReviews(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RATING_CHOICE = [
        (1, '1 - Excellent'),
        (2, '2 - Very nice'),
        (3, '3 - Nice'),
        (4, '2 - Normal'),
        (5, '2 - Not so good in taste'), 
    ]
    rating = models.IntegerField(choices=RATING_CHOICE)
    date_added = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# Many to many
class store(models.Model):
    name = models.CharField(max_length=100)
    location =models.CharField(max_length=100)
    ChaiVarieties = models.ManyToManyField(ChaiVariety, related_name='stores')
    
    def __str__(self):
        return self.name
    
# One to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now) 
    valid_until = models.DateTimeField()   
    
    def __str__(self):
        return f'Certificate for {self.chai.name}'