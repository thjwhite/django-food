from django.db import models

from code_snippets.models import Snippet
from recipes.models import Recipe


class BlogEntry(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    paragraph = models.TextField()


class Section(models.Model):
    blog_entry = models.ForeignKey(BlogEntry)
    order_id = models.IntegerField()
    header = models.CharField(max_length=255)

    def __str__(self):
        return self.header

    class Meta:
        unique_together = (("order_id", "blog_entry"), )


class Part(models.Model):
    order_id = models.IntegerField()
    section = models.ForeignKey(Section)
    paragraph = models.OneToOneField(Paragraph)
    code = models.OneToOneField(Snippet)
    recipe = models.OneToOneField(Recipe)

    class Meta:
        unique_together = (("order_id", "section"), )
