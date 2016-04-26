from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class IngredientRequirement(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    measurement_unit = models.CharField(max_length=255)
    number_required = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "[%s %s %s]" % (self.number_required, self.measurement_unit, str(self.ingredient))
