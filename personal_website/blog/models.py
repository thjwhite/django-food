from django.db import models

from code_snippets.models import Snippet
from recipes.models import Recipe


class BlogEntry(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Section(models.Model):
    blog_entry = models.ForeignKey(BlogEntry)
    order_id = models.IntegerField()
    header = models.CharField(max_length=255)

    def __str__(self):
        return self.header

    class Meta:
        unique_together = (("order_id", "blog_entry"), )
        ordering = ['order_id']


class Link(models.Model):
    link = models.URLField()
    caption = models.CharField(max_length=255)


class Photo(models.Model):
    photo = models.ImageField(upload_to="images/%Y/%m/%d/")
    alt = models.CharField(max_length=255, null=True, blank=True)


class Part(models.Model):
    order_id = models.IntegerField()
    section = models.ForeignKey(Section)
    paragraph = models.TextField()
    code = models.OneToOneField(Snippet, null=True, blank=True)
    recipe = models.OneToOneField(Recipe, null=True, blank=True)
    photo = models.OneToOneField(Photo, null=True, blank=True)
    link = models.OneToOneField(Link, null=True, blank=True)

    class Meta:
        unique_together = (("order_id", "section"), )
        ordering = ['order_id']
