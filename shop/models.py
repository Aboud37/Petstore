from datetime import timezone, datetime, date
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from accounts.models import *

# Create your models here.

class Cover(models.Model):
    big_cover_img = models.ImageField(null=False, blank=False, upload_to="seting_image/")
    small_cover_img = models.ImageField(null=False, blank=False, upload_to="seting_image/")
    cover_title= models.CharField(null=False, blank=False, max_length=30, default='null')

    def __str__(self):
        return self.cover_title

class Section1(models.Model):
    section1_img= models.ImageField(null=False, blank=False, upload_to="seting_image/")
    section1_desc = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.section1_desc

class Section2(models.Model):
    section2_title = models.CharField(null=False, blank=False, max_length=20)
    section2_desc1 = models.CharField(null=False, blank=False, max_length=30, default="null")
    section2_desc2 = models.CharField(null=False, blank=False, max_length=30, default="null")
    section2_img = models.ImageField(null=True, blank=False, upload_to="seting_image/")

    def __str__(self):
        return self.section2_desc1

class Testimonial(models.Model):
    title = models.CharField(null=False, blank=False, max_length=30)
    name = models.CharField(null=False, blank=False, max_length=30)
    location = models.CharField(null=False, blank=False, max_length=30)
    description = models.TextField(null=False, blank=False, max_length=5000)
    img = models.ImageField(null=True, blank=False, upload_to="seting_image/")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SellAPet(models.Model):
    sexe_choices =(('Male','Male'),('Female','Female'))

    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account)
    race = models.ForeignKey(Race, null=True, blank=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank= True)
    address = models.CharField(max_length=1000, blank=True)
    price = models.FloatField(blank=False)
    quantity = models.IntegerField(blank=False)
    sexe = models.CharField(max_length=250, choices=sexe_choices)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image1= models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image2 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image3 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)+ " " + ":" + " "+ str(self.category)




class SitAPet(models.Model):
    sexe_choices =(('Male','Male'),('Female','Female'))

    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account)
    race = models.ForeignKey(Race, null=True, blank=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank= True)
    address = models.CharField(max_length=1000, blank=True)
    price = models.FloatField(blank=False)
    sexe = models.CharField(max_length=250, choices=sexe_choices)
    pets = models.BooleanField(max_length=250, blank=True, null=True)
    garden = models.BooleanField(max_length=250, blank=True, null=True)
    house = models.BooleanField(max_length=250,blank=True, null=True )
    available_from = models.DateField(blank=False)
    available_to = models.DateField(blank=False)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image1= models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image2 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image3 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)+ " " + ":" + " "+ str(self.category)


class SellFood(models.Model):

    brand = models.CharField(max_length=250,)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account)
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank= True)
    price = models.FloatField(blank=False)
    quantity = models.FloatField(blank=False)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image1= models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image2 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image3 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)+ " " + ":" + " "+ str(self.brand)



class DonateAPet(models.Model):
    sexe_choices =(('Male','Male'),('Female','Female'))

    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account)
    race = models.ForeignKey(Race, null=True, blank=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank= True)
    address = models.CharField(max_length=1000, blank=True)
    quantity = models.IntegerField(blank=False)
    sexe = models.CharField(max_length=250, choices=sexe_choices)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image1= models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image2 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    image3 = models.ImageField(null=True, blank=True, upload_to="seting_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)+ " " + ":" + " "+ str(self.category)

