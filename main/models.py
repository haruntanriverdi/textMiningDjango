from django.db import models
from django.utils.functional import cached_property

from main import create_model as cm




class Main(models.Model):
    true_caption = models.CharField(max_length=11200)
    caption = models.CharField(max_length=11200)
    upload1 = models.ImageField()
    upload2 = models.ImageField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):

        #self.slug = slugify(self.title)
        super(Main, self).save(*args, **kwargs)