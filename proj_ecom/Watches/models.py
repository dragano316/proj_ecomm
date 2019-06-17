import random
import os
from django.db import models
from retailer_profile.models import Retailer



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 868686)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return "watch/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Watch(models.Model):
    watch_id = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    category=models.CharField(max_length=120)
    type=models.CharField(max_length=120)
    brand=models.CharField(max_length=120)

    def __str__(self):
        return self.watch_id