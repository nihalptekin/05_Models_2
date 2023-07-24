from django.db import models

# Create your models here.


class Account(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField(null=True)
    # profile=models.OneToOneField(Profile, on_delete=models.CASCADE) # IKISI BIRDEN OLMAZ
    #BIRISINI PRIMARYKEY DIGHERININ FOREIGN KEY OLMASI LAZIM. 
    def __str__(self):
        return self.username

class Profile(models.Model):
    name= models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    about= models.TextField(null=True)
    phone= models.BigIntegerField(null=True)
    avatar=models.ImageField('userpicture', 
                             blank=True, null=True, upload_to='media/')
    account=models.OneToOneField(Account, on_delete=models.CASCADE)  
    #on_delete anlami: bu nesne silindigi zaman acoounta ne olacak?
    # * CASCADE yazdik. bunu yazdigimiz icin primary silinince foreign olan de silinecek. SUAN PRIMARY ACCOUNT. 
    # * SETNULL  Null olarak günceller. account_id numm yaapr mesela
    # * DO_NOTHING filed odlugu gäbä klair
    # * SET_DEFAULT istenilen bir deger atanir
    # * PROTECT Silmeye izin vermez



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="profile about user"
        verbose_name_plural="Users profile"

class Adress(models.Model):
    name=models.CharField(max_length=20)
    adress=models.TextField(null=True)
    account=models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    productname=models.CharField(max_length=20)
    account=models.ManyToManyField(Account)

    def __str__(self):
        return self.pruductname
    

# kur
    # python -m pip install Pillow
    # settings.py a ekle
    # MEDIA_URL = 'media/
    # urls.py a ekle
    # from django.conf import settings
    # from django.conf.urls.static import static
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)