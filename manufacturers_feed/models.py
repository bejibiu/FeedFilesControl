from django.db import models

BRAND_LEN = 200


class Brand(models.Model):
    name = models.CharField(max_length=BRAND_LEN)


class Feed(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    feed_file = models.FileField(upload_to=brand.name)
