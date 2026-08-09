from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Channel(models.Model):
    CATEGORY_CHOICES = [
        ('smartphones', 'Smartphones'),
        ('pc_hardware', 'PC Hardware'),
        ('programming', 'Programming'),
        ('ai', 'AI / Machine Learning'),
        ('cybersecurity', 'Cybersecurity'),
        ('gaming_tech', 'Gaming Tech'),
        ('consumer_tech', 'Consumer Tech'),
        ('tech_news', 'Tech News'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    creator_name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    subscribers = models.PositiveIntegerField()
    youtube_url = models.URLField()
    image = models.ImageField(upload_to='channel_images/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('channel_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)