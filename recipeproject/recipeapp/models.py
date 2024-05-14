from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name_category = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name_category}'


class Recipes(models.Model):
    name_recipe = models.CharField(max_length=150)
    description_recipe = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.TimeField()
    image_recipe = models.ImageField(upload_to='recipes/')
    author_recipe = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_recipe}'
