from ast import arg
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class Campaign(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    slug=models.SlugField(max_length=255, editable=False)
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.DateField.auto_now
    # auto_now_add, updated when the record is added    
    created_at=models.DateTimeField(auto_now_add=True)
    # auto_now updated when the record is updated 
    updated_at=models.DateTimeField(auto_now=True)
    logo=CloudinaryField('Image', overwrite=True, blank=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        to_assign=slugify(self.title)
        # slug must be unique
        if Campaign.objects.filter(slug=to_assign).exists():
            to_assign += str(Campaign.objects.all().count)
        self.slug=to_assign
        super().save(*args, **kwargs)


class Subscriber(models.Model):
    campaign=models.ForeignKey(to=Campaign, on_delete=models.DO_NOTHING)
    email=models.EmailField(max_length=254)
    # auto_now_add, updated when the record is added    
    created_at=models.DateTimeField(auto_now_add=True)
    # auto_now updated when the record is updated 
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return self.email
