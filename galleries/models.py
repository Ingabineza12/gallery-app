from django.db import models

# Create your models here.

import datetime as dt

class Photographer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    def __str__(self):
        return self.first_name
    def save_photographer(self):
        self.save()
    def delete_photographer(self):
        self.delete()
    @classmethod
    def display_photographers(cls):
        photographers=Photographer.objects.all()
        for photographer in photographers:
            return photographer
    class Meta:
        ordering=['first_name']


class Location(models.Model):
    photo_location=models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self,update):
        self.photo_location=update
        self.save()
    @classmethod
    def get_location_id(cls,id):
        locate=Location.objects.get(pk=id)
        return locate

    def __str__(self):
        return self.photo_location

class Category(models.Model):
    photo_category=models.CharField(max_length=30)

    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

    def update_category(self,update):
        self.photo_category=update
        self.save()
    @classmethod
    def get_category_id(cls,id):
        category=Category.objects.get(pk=id)
        return category

    @classmethod
    def search_by_category(cls,id):
        category=Category.objects.get(pk=id)
        return category

    def __str__(self):
        return self.photo_category

class Image(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=30)
    image=models.ImageField(upload_to='images_galleries/')
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    photographer=models.ForeignKey(Photographer,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering=('-id',)
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

    def update_category(self,update):
        self.photo_category=update
        self.save()

    @classmethod
    def get_all_image(cls):
        all_images=Image.objects.all()
        return all_images

    @classmethod
    def get_image_by_id(cls,id):
        an_image=Image.objects.get(id=id)
        return an_image

    def __str__(self):
        return self.title
    @classmethod
    def search_by_category(cls,search_term):
        photo=cls.objects.filter(category__photo_category__icontains=search_term)
        return photo

    @classmethod
    def filter_by_location(cls,id):
        images=Image.objects.filter(location_id=id)
        return images
