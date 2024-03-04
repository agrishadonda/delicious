from django.db import models

# Create your models here.
class card(models.Model):
    tital = models.CharField(max_length = 20)
    content = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.tital
    
class banners(models.Model):
    image = models.ImageField(upload_to='images/')
    content1 = models.CharField(max_length = 300)
    name  = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class controls(models.Model):
    img = models.ImageField(upload_to='images/')
    titals = models.CharField(max_length = 100)
    date = models.DateField()
    para = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.para
    
class details(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    subjet = models.CharField(max_length = 20)
    message = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
