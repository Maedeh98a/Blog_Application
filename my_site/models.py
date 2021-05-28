from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().filter(status='publish')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('publish', 'publish'),
    )
    title = models.CharField(max_length=50, verbose_name='عنوان')
    slug = models.SlugField(max_length=30, allow_unicode=True, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)
        db_table = 'post'
        verbose_name = 'پست '
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('my_site:detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    objects = models.Manager()
    published = PostManager()