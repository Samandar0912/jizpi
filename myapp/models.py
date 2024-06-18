from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Ekran Rasmi
class ekranImages(models.Model):
    name = models.CharField( max_length=50)
    img = models.ImageField(upload_to='Photos/ekran_IMG/',)

    class Meta:
        verbose_name = "Ekran Rasmi"
        verbose_name_plural ="Ekran Rasmlari"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ekranImages_detail", kwargs={"pk": self.pk})

# Category Yangiliklar (News)

    
class ArticleNews(models.Model):
    title = models.CharField( max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='Tana qismi')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    created_at = models.DateTimeField( auto_now_add=True)
   
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ArticleNews_details", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["-id"]
        verbose_name="Yangilik"
        verbose_name_plural="Yangiliklar"
        
    
  
    
class ArticleElon(models.Model):
    title = models.CharField( max_length=200, verbose_name='Sarlovha')
    body = models.TextField(verbose_name='Tana qismi')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    img1 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img2 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    img3 = models.ImageField(blank=True, upload_to='Photos/Yangiliklar/',)
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("ArticleElon_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ["-id"]
        verbose_name="Elon"
        verbose_name_plural="Elonlar"
        
        


class ArticleKafedra(models.Model):
    title = models.CharField(max_length=200, verbose_name='Kafedra nomi')
    name = models.CharField(max_length=200, verbose_name='Kafedra mudiri FISH')
    img = models.ImageField(upload_to='Photos/Yangiliklar/',)
    qabul = models.CharField(max_length=200, verbose_name='qabul vaqti')
    telRaqam = models.CharField(max_length=200, verbose_name='Raqami')
    mail = models.EmailField( max_length=254, verbose_name='email')
    text = models.TextField(verbose_name='batafsil')
    
    img1 = models.ImageField(upload_to='Photos/Yangiliklar/',verbose_name='kafedra rasmi-1')
    img2 = models.ImageField(upload_to='Photos/Yangiliklar/',verbose_name='kafedra rasmi-2')
    
    
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name="Kafedra"
        verbose_name_plural="Kafedralar"
    
    def get_absolute_url(self):
        return reverse('kafedra_detail', kwargs={"pk": self.pk})
    