from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField()


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class IngredientRequirement(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    measurement_unit = models.CharField(max_length=255)
    number_required = models.DecimalField(max_digits=5, decimal_places=2)
