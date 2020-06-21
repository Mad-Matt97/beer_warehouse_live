from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING

from beers.utils import image_upload_location
from core.models import CommonInfo


class Company(CommonInfo):
    name = models.CharField('Name', max_length=200)
    tax_number = models.IntegerField('Tax Number', unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_CHOICES = (
        (1, 'Yellow'),
        (2, 'Brown'),
        (3, 'Black')
    )

    name = models.CharField('Name', max_length=100)
    abv = models.DecimalField('Alcohol', max_digits=3, max_length=2, default=0, decimal_places=2)
    is_filtered = models.BooleanField('Filtered', default=False)
    color = models.PositiveSmallIntegerField('Color', choices=COLOR_CHOICES, default=1)
    image = models.ImageField('Image', blank=True, null=True, upload_to=image_upload_location)
    company = models.ForeignKey(Company, related_name="beers", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Beer'
        verbose_name_plural = 'Beers'
        ordering = ['-name']

    def __str__(self):
        return self.name

    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alcohol_than(self, alcohol):
        return self.abv > alcohol


class SpecialIngredient(CommonInfo):
    name = models.CharField('Name', max_length=50)
    beers = models.ManyToManyField(Beer, blank=True, related_name='special_ingredients')

    class Meta:
        verbose_name = 'Special_Ingredient'
        verbose_name_plural = 'Special_Ingredients'
        ordering = ['-name']

    def __str__(self):
        return self.name
