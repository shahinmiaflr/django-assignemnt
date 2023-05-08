from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        suffix = 2
        original_slug = self.slug

        while PostCategory.objects.filter(slug=self.slug).exists():
            self.slug = f'{original_slug}-{suffix}'
            suffix += 1
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class BlogPost(models.Model):

    STATUS = [
        ('draft','Draft'),
        ('published','Publish'),
        ('slider','Slider')
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = RichTextUploadingField()
    feature_img = models.ImageField(upload_to='media/blog/image/', blank=True,null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True,)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            suffix = 2
            original_slug = self.slug

        while BlogPost.objects.filter(slug=self.slug).exists():
            self.slug = f'{original_slug}-{suffix}'
            suffix += 1
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'All Polsts'