import os
from django.db import models
from django.utils.text import slugify


class Dog(models.Model):

    initial_id = models.IntegerField(db_index=True, default=0)
    slug = models.SlugField(db_index=True, max_length=255, unique=True, null=True)
    name = models.CharField(db_index=True, max_length=255, null=True, blank=True)
    bred_for = models.TextField(null=True, blank=True)
    breed_group = models.TextField(null=True, blank=True)

    weight = models.JSONField(default=dict)

    height = models.JSONField(default=dict)

    image = models.JSONField(default=dict)

    origin = models.TextField(null=True, blank=True)

    reference_image_id = models.CharField(
        db_index=True, max_length=255, null=True, blank=True
    )

    life_span = models.TextField(null=True, blank=True)

    temperament = models.TextField(null=True, blank=True)

    prepopulated_fields = {"slug": ("name",)}
    
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Dog.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        """Creates a slug based on Dog name
        Example:
        Name: TheBadOne
        Slug: TheBadOne-1
        """
        self.slug = self._get_unique_slug()
        super(Dog, self).save(*args, **kwargs)
        
        
    # def long_life_span_dogs(self):
    #     Dog.objects.
        
        
    # @classmethod
    # def successful(cls):
    #     return cls.objects.get(code=0)

    def __str__(self):
        """Returns a name of the dog as object representation"""

        return self.name
